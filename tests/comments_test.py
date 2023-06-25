import unittest
import requests

from burrito.utils.config_reader import get_config

from auth_test import AuthTestCase
from tickets_test import create_ticket_get_id
from utils.exceptions_tool import check_error


TIMEOUT = 5


class CommentsTestCase(unittest.TestCase):
    def test_001_comments_create(self):
        response = requests.post(
            f"http://{get_config().BURRITO_HOST}:{get_config().BURRITO_PORT}/comments/create",
            headers={
                "Authorization": f"Bearer {AuthTestCase.access_token}"
            },
            json={
                "ticket_id": create_ticket_get_id("Make comment"),
                "body": "ya perdole kurva"
            },
            timeout=TIMEOUT
        )

        check_error(
            self.assertEqual,
            {
                "first": response.status_code,
                "second": 200
            },
            response
        )

        return response.json()["comment_id"]

    def test_002_comments_edit(self):
        response = requests.post(
            f"http://{get_config().BURRITO_HOST}:{get_config().BURRITO_PORT}/comments/edit",
            headers={
                "Authorization": f"Bearer {AuthTestCase.access_token}"
            },
            json={
                "comment_id": self.test_001_comments_create(),
                "body": "ya perdole kurva (edited)"
            },
            timeout=TIMEOUT
        )

        check_error(
            self.assertEqual,
            {
                "first": response.status_code,
                "second": 200
            },
            response
        )

    def test_003_comments_delete(self):
        response = requests.delete(
            f"http://{get_config().BURRITO_HOST}:{get_config().BURRITO_PORT}/comments/delete",
            headers={
                "Authorization": f"Bearer {AuthTestCase.access_token}"
            },
            json={
                "comment_id": self.test_001_comments_create()
            },
            timeout=TIMEOUT
        )

        check_error(
            self.assertEqual,
            {
                "first": response.status_code,
                "second": 200
            },
            response
        )
