from fastapi import HTTPException, Depends
from fastapi_jwt_auth import AuthJWT

from burrito.schemas.user_schema import UserPasswordLoginSchema
from burrito.schemas.auth_schema import AuthSettingsModel

from burrito.models.user_model import Users

from burrito.utils.db_utils import get_user_by_login
from burrito.utils.hash_util import compare_password


@AuthJWT.load_config
def get_config():
    return AuthSettingsModel()


def password_login(user_login_data: UserPasswordLoginSchema, Authorize: AuthJWT = Depends()):
    """Authentication by login and password"""

    user: Users | bool = get_user_by_login(user_login_data.login)

    if user:
        # if user login exist we can compare password and hashed password

        if compare_password(user_login_data.password, user.password):
            access_token = Authorize.create_access_token(
                subject=user_login_data.login
            )

            return {"access_token": access_token}

        else:
            raise HTTPException(
                status_code=401,
                detail="Password is incorrect"
            )

    raise HTTPException(status_code=401, detail="Login is not exist")


def token_login(Authorize: AuthJWT = Depends()):
    """
        Authentication by access token. It will return new access token ^_^
    """

    Authorize.jwt_required()

    return {
        "access_token": Authorize.create_access_token(
            subject=Authorize.get_jwt_subject()
        )
    }
