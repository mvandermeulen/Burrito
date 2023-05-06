from burrito.models.tickets_model import Tickets
from burrito.models.roles_model import Roles
from burrito.models.statuses_model import Statuses
from burrito.models.tags_model import Tags
from burrito.models.user_model import Users
from burrito.models.faculty_model import Faculties
from burrito.models.group_model import Groups

from burrito.models.comments_model import Comments
from burrito.models.actions_model import Actions
from burrito.models.participants_model import Participants
from burrito.models.queues_model import Queues
from burrito.models.notifications_model import Notifications
from burrito.models.subscriptions_model import Subscriptions

from burrito.models.bookmarks_model import Bookmarks

from burrito.schemas.profile_schema import UpdateProfileSchema

from burrito.utils.db_cursor_object import get_database_cursor
from burrito.utils.logger import get_logger


def setup_database():
    """_summary_

    Setup database. Insert base roles, etc
    """


def create_tables():
    """_summary_

    Create all tables using models in burrito/models
    """

    get_database_cursor().create_tables(
        (
            Users, Roles, Faculties, Groups,
            Roles, Tags, Statuses,
            Tickets, Participants,
            Subscriptions, Actions, Notifications,
            Comments, Queues, Bookmarks
        )
    )
    get_logger().info("All tables was created")


def drop_tables(use: bool = False):
    """_summary_

    Drop all tables in database

    Args:
        use (bool, optional): To confirm the reset of the table . Defaults to False.
    """

    if not use:
        return

    get_database_cursor().drop_tables(
        (
            Roles, Tags, Statuses,
            Tickets, Users, Participants,
            Subscriptions, Actions, Notifications,
            Groups, Faculties, Comments, Queues, Bookmarks
        )
    )
    get_logger().warning("All tables was dropped")


def create_user(login: str, hashed_password: str) -> int | None:
    """_summary_

    Create user with default fields: (login, hashed_password)

    Args:
        login (str): user login
        hashed_password (str): user hashed password

    Returns:
        bool: status creating new user
    """

    try:
        user: Users = Users.create(
            login=login, password=hashed_password
        )
        return user.user_id

    except Exception as e:  # pylint: disable=broad-except
        get_logger().error(e)


def update_user(user: Users, data: UpdateProfileSchema) -> None:
    """_summary_

    Args:
        user (Users): user object
        data (UpdateProfileSchema): new updates for user profile
    """

    if data.firstname:
        user.firstname = data.firstname

    if data.lastname:
        user.lastname = data.lastname

    if data.phone:
        user.phone = data.phone

    if data.email:
        user.email = data.email

    user.save()  # save updates


def get_user_by_login(login: str) -> Users | None:
    """_summary_

    Get user if exist or return None

    Args:
        login (str): user login

    Returns:
        Users | None: return None if user is not exist
    """

    try:
        return Users.get(Users.login == login)
    except Exception:  # pylint: disable=broad-except
        return


def get_user_by_id(user_id: int) -> Users | None:
    """_summary_

    Get user if exist or return None

    Args:
        user_id (int): user id

    Returns:
        Users | None: return None if user is not exist
    """

    try:
        return Users.get(Users.user_id == user_id)
    except Exception:  # pylint: disable=broad-except
        return
