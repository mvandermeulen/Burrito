from peewee import AutoField, CharField, IntegerField

from burrito.models.basic_model import BurritoBasicModel


class StatusesStatistic(BurritoBasicModel):
    status_id = AutoField()
    name = CharField(32)
    tickets_count = IntegerField(null=False)

    def __str__(self) -> str:
        return f"{self.status_id} {self.name} {self.tickets_count}"


class FacultyScopesStatistic(BurritoBasicModel):
    faculty_id = AutoField()
    name = CharField()
    reports_count = CharField(column_name="Reports")
    qa_count = CharField(column_name="Q/A")
    suggestion = CharField(column_name="Suggestion")

    def __str__(self) -> str:
        return f"{self.faculty_id} {self.name}"


class ScopesStatistic(BurritoBasicModel):
    scope = CharField()
    tickets_count = IntegerField()

    def __str__(self) -> str:
        return f"{self.scope} {self.tickets_count}"
