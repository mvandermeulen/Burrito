import datetime

from peewee import (
    Model, CharField, PrimaryKeyField,
    DateTimeField, ForeignKeyField
)

from burrito.models.tickets_model import Tickets
from burrito.models.user_model import Users

from burrito.utils.db_cursor_object import get_database_cursor


class Actions(Model):
    action_id = PrimaryKeyField()
    ticket_id = ForeignKeyField(
        Tickets,
        to_field="ticket_id",
        on_delete="NO ACTION"
    )
    user_id = ForeignKeyField(Users, to_field="user_id", on_delete="NO ACTION")

    action_date = DateTimeField(default=datetime.datetime.now)

    field_name = CharField(max_length=255)
    old_value = CharField(max_length=255)
    new_value = CharField(max_length=255)

    class Meta:
        database = get_database_cursor()
