import datetime

from peewee import (
    Model, PrimaryKeyField,
    IntegerField, TextField,
    DateTimeField, BooleanField,
    CharField, ForeignKeyField
)

from burrito.models.tags_model import Tags
from burrito.models.statuses_model import Statuses
from burrito.models.faculty_model import Faculties
from burrito.models.user_model import Users

from burrito.utils.db_cursor_object import get_database_cursor


class Tickets(Model):
    ticket_id = PrimaryKeyField()

    creator = ForeignKeyField(
        Users,
        to_field="user_id",
        on_delete="NO ACTION"
    )
    assignee = ForeignKeyField(
        Users,
        to_field="user_id",
        on_delete="NO ACTION",
        null=True
    )

    subject = CharField(255)
    body = TextField()

    hidden = BooleanField(default=False)
    anonymous = BooleanField(default=False)

    upvotes = IntegerField(default=0)

    created = DateTimeField(default=datetime.datetime.now)

    faculty_id = ForeignKeyField(
        Faculties,
        to_field="faculty_id",
        on_delete="NO ACTION"
    )
    tag_id = ForeignKeyField(
        Tags,
        to_field="tag_id",
        on_delete="NO ACTION"
    )
    status_id = ForeignKeyField(
        Statuses,
        to_field="status_id",
        on_delete="NO ACTION"
    )

    class Meta:
        database = get_database_cursor()
        depends_on = [Users, Faculties, Tags, Statuses]
