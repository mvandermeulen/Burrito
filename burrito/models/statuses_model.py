from peewee import Model, PrimaryKeyField, CharField

from burrito.utils.db_cursor_object import get_database_cursor


class Statuses(Model):
    status_id = PrimaryKeyField()
    name = CharField(32)

    class Meta:
        database = get_database_cursor()
