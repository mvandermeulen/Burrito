from typing import Any
from playhouse.shortcuts import model_to_dict

from fastapi import Response

from burrito.models.statuses_model import Statuses
from burrito.models.group_model import Groups
from burrito.models.faculty_model import Faculties
from burrito.models.queues_model import Queues
from burrito.models.user_model import Users

from burrito.schemas.meta_schema import (
    ResponseStatusesListSchema,
    ResponseGroupsListSchema,
    ResponseFacultiesListSchema,
    RequestQueueListSchema,
    ResponseQueueListSchema,
    ResponseAdminListSchema
)
from burrito.schemas.group_schema import GroupResponseSchema
from burrito.schemas.faculty_schema import FacultyResponseSchema
from burrito.schemas.status_schema import StatusResponseSchema
from burrito.schemas.queue_schema import QueueResponseSchema

from burrito.utils.converter import FacultyConverter
from burrito.utils.tickets_util import make_short_user_data
from burrito.utils.query_util import ADMIN_ROLES


_ICON_FILE = None
with open("burrito/resources/general_icon.png", "rb") as file:
    _ICON_FILE = file.read()



async def meta__get_statuses_list():
    return ResponseStatusesListSchema(
        statuses_list=[
            StatusResponseSchema(**model_to_dict(s)) for s in Statuses.select()
        ]
    )


async def meta__get_groups_list():
    return ResponseGroupsListSchema(
        groups_list=[
            GroupResponseSchema(
                **model_to_dict(group)
            ) for group in Groups.select()
        ]
    )


async def meta__faculties_list():
    return ResponseFacultiesListSchema(
        faculties_list=[
            FacultyResponseSchema(
                **model_to_dict(faculty)
            ) for faculty in Faculties.select()
        ]
    )


async def meta__get_queues_list(faculty_data: RequestQueueListSchema):
    faculty_object = FacultyConverter.convert(faculty_data.faculty)

    response_list: list[QueueResponseSchema] = []
    for queue in Queues.select().where(
        Queues.faculty == faculty_object
    ):
        queue = model_to_dict(queue)
        queue["faculty"] = faculty_object.faculty_id

        response_list.append(
            QueueResponseSchema(
                **queue
            )
        )

    return ResponseQueueListSchema(queues_list=response_list)


async def meta__get_admins():
    return ResponseAdminListSchema(
        admin_list=[
            make_short_user_data(
                admin,
                hide_user_id=False
            ) for admin in Users.select().where(Users.role.in_(ADMIN_ROLES))
        ]
    )


async def meta__cabinet_meta_root(key: str = "", mode: int = 256, flag: int = 0, params: Any = None):
    match mode:
        case 0:
            ...

        case 1:
            return Response(
                content="<b>Сервіс зроблений жоскими челіками</b>",
                media_type="text/html"
            )

        case 2:
            return Response(
                content=_ICON_FILE,
                media_type="image/png"
            )

        case 3:
            return Response(
                content="Тікетингова система для написання скарг/пропозицій/запитань",
                media_type="text/plain"
            )

        case 100:
            ...

        case _:
            ...
