from fastapi import Depends, status, HTTPException
from fastapi.responses import JSONResponse

from burrito.schemas.registration_schema import RegistrationSchema

from burrito.models.user_model import Users
from burrito.models.m_email_code import EmailVerificationCode

from burrito.schemas.email_code import EmailVerificationCodeSchema

from burrito.utils.converter import GroupConverter, FacultyConverter
from burrito.utils.mongo_util import mongo_insert, mongo_select, mongo_delete
from burrito.utils.hash_util import generate_email_code, get_hash
from burrito.utils.email_util import tmp_send_email
from burrito.utils.auth import get_auth_core, BurritoJWT, AuthTokenPayload

from .utils import (
    create_user, get_user_by_login,
    is_valid_login, is_valid_password
)


EMAIL_VERIFICATIONS_TEMPLATE = """Добрий день,


Ваш запит на реєстрацію в проекті TreS було успішно оброблено.
Для завершення реєстрації, будь ласка, введіть нижче наведений код підтвердження:

{}

Будь ласка, уважно перевірте введений код та переконайтеся, що він відповідає наданому вам під час реєстрації.
Якщо у вас виникли будь-які труднощі чи потребуються додаткові вказівки, будь ласка, зв'яжіться з нашою службою підтримки.


З повагою,

Команда TreS
"""


async def registration__user_registration(
    user_data: RegistrationSchema
):
    """Handle user registration"""

    if not is_valid_login(user_data.login):
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={"detail": "Invalid login"}
        )

    if not is_valid_password(user_data.password):
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={"detail": "Invalid password"}
        )

    if get_user_by_login(user_data.login):
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={"detail": "User with the same login exist"}
        )

    if mongo_select(
        EmailVerificationCode,
        login=user_data.login
    ):
        raise HTTPException(
            status_code=403,
            detail="User with the same login is in registration process"
        )

    if user_data.group is not None:
        GroupConverter.convert(user_data.group)
    FacultyConverter.convert(user_data.faculty)

    verification_code = generate_email_code()
    mongo_insert(
        EmailVerificationCode(
            hashed_code=get_hash(
                verification_code,
                b"super_mega_long_salt_(it will be removed in soon)"
            ),
            firstname=user_data.firstname,
            lastname=user_data.lastname,
            login=user_data.login,
            password=get_hash(user_data.password),
            group=user_data.group,
            faculty=user_data.faculty,
            phone=user_data.phone,
            email=user_data.email
        )
    )

    tmp_send_email(
        user_data.email,
        "Підтвердження реєстрації в TreS",
        EMAIL_VERIFICATIONS_TEMPLATE.format(verification_code)
    )

    return {
        "status": "OK"
    }


async def registration__verify_email(
    verification_data: EmailVerificationCodeSchema,
    __auth_obj: BurritoJWT = Depends(get_auth_core())
):
    email_code = mongo_select(
        EmailVerificationCode,
        hashed_code=get_hash(
            verification_data.email_code,
            b"super_mega_long_salt_(it will be removed in soon)"
        )
    )

    if not email_code:
        raise HTTPException(
            status_code=403,
            detail="Invalid code received"
        )
    email_code = email_code[0]

    current_user: Users | None = create_user(
        RegistrationSchema(
            **email_code
        )
    )

    if current_user:
        result = (await __auth_obj.create_token_pare(
            AuthTokenPayload(
                user_id=current_user.user_id,
                role=current_user.role.name
            )
        )) | {"user_id": current_user.user_id}

        mongo_delete(
            EmailVerificationCode,
            _id=email_code["_id"]
        )

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=result
        )

    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detail": "..."}
    )
