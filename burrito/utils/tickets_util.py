from typing import Any

from fastapi import HTTPException, status

from playhouse.shortcuts import model_to_dict

from burrito.models.bookmarks_model import Bookmarks
from burrito.models.tickets_model import Tickets
from burrito.models.actions_model import Actions
from burrito.models.user_model import Users

from burrito.schemas.action_schema import ActionSchema
from burrito.schemas.tickets_schema import TicketUsersInfoSchema
from burrito.schemas.faculty_schema import FacultyResponseSchema


def is_ticket_exist(ticket_id: int) -> Tickets | None:
    """_summary_

    Args:
        ticket_id (int): ticket ID

    Returns:
        Tickets | None: return ticket object if exist else return None
    """

    _ticket = Tickets.get_or_none(
        Tickets.ticket_id == ticket_id
    )

    if not _ticket:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"ticket_id {ticket_id} is not exist"
        )

    return _ticket


def am_i_own_this_ticket(ticket_creator_id: int, user_id: int) -> bool:
    return ticket_creator_id == user_id


def am_i_own_this_ticket_with_error(
    ticket_creator_id: int, user_id: int
) -> bool | None:
    if not am_i_own_this_ticket(ticket_creator_id, user_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You have not permissions to interact with this ticket"
        )

    return True


def hide_ticket_body(body: str, result_length: int = 500) -> str:
    return body[:result_length] + ("..." if len(body) >= result_length else "")


def make_short_user_data(
    user: Users,
    *,
    hide_user_id: bool = True
) -> TicketUsersInfoSchema:
    user_dict_data = model_to_dict(user)
    user_dict_data["faculty"] = FacultyResponseSchema(
        **model_to_dict(user.faculty)
    )

    if hide_user_id:
        user_dict_data["user_id"] = None
        user_dict_data["group"] = None

    return TicketUsersInfoSchema(**user_dict_data)


def is_ticket_bookmarked(user_id: int, ticket_id: int) -> bool:
    return bool(
        Bookmarks.get_or_none(
            Bookmarks.user_id == user_id,
            Bookmarks.ticket_id == ticket_id
        )
    )


def select_filters(available_filters: dict[str, Any], received_filters) -> list[Any]:
    final_filters = []
    for filter_name, value in received_filters.dict().items():
        filter_candidate = available_filters.get(filter_name)
        if filter_candidate is not None and value:
            final_filters.append(filter_candidate)
    return final_filters


def get_filtered_tickets(
    _filters: list[Any],
    _desc: bool = True,
    start_page: int = 1,
    tickets_count: int = 10
) -> list[Tickets]:
    if _filters:
        return Tickets.select().where(*_filters).paginate(
            start_page,
            tickets_count
        ).order_by(
            Tickets.created.desc() if _desc else Tickets.created
        )

    return Tickets.select().paginate(
        start_page,
        tickets_count
    ).order_by(
        Tickets.created.desc() if _desc else Tickets.created
    )


def create_ticket_action(
    *,
    ticket_id: int,
    author_id: int,
    field_name: str,
    old_value: str,
    new_value: str
) -> None:
    Actions.create(
        ticket=ticket_id,
        author=author_id,
        field_name=field_name,
        old_value=old_value,
        new_value=new_value
    )


def get_ticket_actions(ticket_id: int) -> list[Actions]:
    return [
        ActionSchema(
            action_id=action.action_id,
            ticket_id=action.ticket_id,
            author_id=action.author_id,
            action_date=str(action.action_date),
            field_name=action.field_name,
            old_value=action.old_value,
            new_value=action.new_value
        ) for action in Actions.select().where(Actions.ticket == ticket_id)
    ]
