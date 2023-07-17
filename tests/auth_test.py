import unittest
import requests

from registration_test import RegistrationTestCase

from burrito.utils.config_reader import get_config
from utils.exceptions_tool import check_error


def do_auth():
    response = requests.post(
        f"http://{get_config().BURRITO_HOST}:{get_config().BURRITO_PORT}/auth/password/login",
        json={
            "login": RegistrationTestCase.random_login,
            "password": RegistrationTestCase.random_password
        },
        timeout=5
    )
    return response.status_code, response.json()


class AuthTestCase(unittest.TestCase):
    """Test authentication system"""

    @classmethod
    def setUpClass(cls):
        cls.access_token: None | str = None

    def test_001_do_password_auth(self):
        """
            Login user in rest API using login and password.
            Recv token to use in the next authentications.
        """

        result: tuple[int, dict] = do_auth()

        access_token = result[1].get("access_token")
        AuthTestCase.access_token = access_token

        check_error(
            self.assertEqual,
            {
                "first": result[0],
                "second": 200
            },
            result[1]
        )

        check_error(
            self.assertIsNotNone,
            {
                "obj": access_token
            },
            result[1]
        )

#    @unittest.skip
    def test_002_do_token_auth(self):
        """
            Login user in rest API using login and password.
            Recv token to use in the next authentications.
        """

        response = requests.post(
            f"http://{get_config().BURRITO_HOST}:{get_config().BURRITO_PORT}/auth/token/login",
            headers={
               "Authorization": f"Bearer {AuthTestCase.access_token}"
            },
            json={
            },
            timeout=5
        )

        check_error(
            self.assertEqual,
            {
                "first": response.status_code,
                "second": 200
            },
            response
        )

    @unittest.skip
    def test_003_do_token_auth_with_old_token(self):
        """
            Login user in rest API using login and password.
            Recv token to use in the next authentications.
        """

        do_auth()

        response = requests.post(
            f"http://{get_config().BURRITO_HOST}:{get_config().BURRITO_PORT}/auth/token/login",
            headers={
               "Authorization": f"Bearer {AuthTestCase.access_token}"
            },
            json={
            },
            timeout=5
        )

        check_error(
            self.assertEqual,
            {
                "first": response.status_code,
                "second": 200
            },
            response
        )
