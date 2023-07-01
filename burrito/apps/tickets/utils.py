from functools import cache

from burrito.utils.auth import get_auth_core
from burrito.utils.users_util import get_user_by_id

from burrito.utils.permissions_checker import check_permission

from burrito.utils.logger import get_logger

from burrito.models.statuses_model import Statuses
from burrito.models.tickets_model import Tickets
from burrito.models.queues_model import Queues
from burrito.models.liked_model import Liked
from burrito.models.user_model import Users

from burrito.schemas.faculty_schema import FacultyResponseSchema
from burrito.schemas.status_schema import StatusResponseSchema
from burrito.schemas.queue_schema import QueueResponseSchema
from burrito.schemas.tickets_schema import (
    UpdateTicketSchema,
    TicketDetailInfoSchema
)

from burrito.utils.auth_token_util import AuthTokenPayload
from burrito.utils.tickets_util import (
    is_ticket_exist,
    am_i_own_this_ticket,
    am_i_own_this_ticket_with_error,
    is_ticket_bookmarked,
    is_ticket_liked,
    get_ticket_actions,
    hide_ticket_body
)


__all__ = (
    "get_auth_core",
    "get_user_by_id",
    "check_permission",
    "is_ticket_exist",
    "am_i_own_this_ticket",
    "am_i_own_this_ticket_with_error"
)


def update_ticket_info(
    ticket_object: Tickets,
    data: UpdateTicketSchema
) -> None:
    if data.subject:
        ticket_object.subject = data.subject

    if data.body:
        ticket_object.body = data.body

    if isinstance(data.hidden, bool):
        ticket_object.hidden = data.hidden

    if isinstance(data.anonymous, bool):
        ticket_object.anonymous = data.anonymous

    ticket_object.save()


@cache
def get_status_close_id() -> Statuses:
    status_name = "CLOSE"
    status_object = Statuses.get_or_none(Statuses.name == status_name)

    if not status_object:
        get_logger().critical(f"Status {status_name} is not exist in database")

    return status_object


def make_ticket_detail_info(
        ticket: Tickets,
        token_payload: AuthTokenPayload,
        creator: Users | None,
        assignee: Users | None,
        *,
        crop_body: bool = True,
        show_history: bool = False
) -> TicketDetailInfoSchema:

    queue: Queues | None = None
    if ticket.queue:
        queue = Queues.get_or_none(Queues.queue_id == ticket.queue)

    return TicketDetailInfoSchema(
        creator=creator,
        assignee=assignee,
        ticket_id=ticket.ticket_id,
        subject=ticket.subject,
        body=hide_ticket_body(ticket.body, 500) if crop_body else ticket.body,
        faculty=FacultyResponseSchema(
            faculty_id=ticket.faculty.faculty_id,
            name=ticket.faculty.name
        ),
        queue=QueueResponseSchema(
            queue_id=queue.queue_id,
            faculty=queue.faculty.faculty_id,
            name=queue.name,
            scope=queue.scope
        ) if queue else None,
        status=StatusResponseSchema(
            status_id=ticket.status.status_id,
            name=ticket.status.name,
        ),
        upvotes=Liked.select().where(
            Liked.ticket_id == ticket.ticket_id
        ).count(),
        is_liked=is_ticket_liked(token_payload.user_id, ticket.ticket_id),
        is_bookmarked=is_ticket_bookmarked(token_payload.user_id, ticket.ticket_id),
        date=str(ticket.created),
        history=get_ticket_actions(ticket.ticket_id) if show_history else []
    )
