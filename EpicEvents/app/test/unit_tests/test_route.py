from django.test import Client
import pytest
from rest_framework.authtoken.models import Token

from app.models import User


client = Client()


dict_correct_admin_user = {"email": "adrien@email.fr", "password": "S3cret!1"}
dict_correct_sales_user = {"email": "michael@email.fr", "password": "S3cret!1"}
dict_correct_support_user = {"email": "kobe@email.fr", "password": "S3cret!1"}


class TestRoute:
    """Class where the routes are tested and should return HTTP 401 Unauthorized."""

    def test_user_route(self):
        response = client.get("/user", follow=True)
        assert response.status_code == 401

    def test_client_route(self):
        response = client.get("/client", follow=True)
        assert response.status_code == 401

    def test_contract_route(self):
        response = client.get("/contract", follow=True)
        assert response.status_code == 401

    def test_event_route(self):
        response = client.get("/event", follow=True)
        assert response.status_code == 401

    def test_event_status_route(self):
        response = client.get("/event_status", follow=True)
        assert response.status_code == 401


@pytest.mark.django_db
class TestCreateUser:
    def test_create_user(self):
        user = User.objects.create_user(
            email="bill@email.fr", role="support", password="S3cret!1"
        )
        assert user.email == "bill@email.fr"
        assert user.is_active == True
        assert user.is_staff == False
        assert user.is_superuser == False
        assert user.role == "support"

    def test_create_superuser(self):
        superuser = User.objects.create_superuser(
            email="testadmin@email.fr", role="management", password="S3cret!1"
        )
        assert superuser.email == "testadmin@email.fr"
        assert superuser.is_active == True
        assert superuser.is_staff == True
        assert superuser.is_superuser == True
        assert superuser.role == "management"


class TestLogin:
    """Class where user login is tested."""

    def test_admin_login(self):
        response = client.post(
            "/admin/login",
            data=dict(dict_correct_admin_user),
            follow=True,
        )
        assert response.status_code == 200

    def test_not_admin_login(self):
        response = client.post(
            "/admin/login",
            data=dict(dict_correct_sales_user),
            follow=True,
        )
        assert response.status_code == 200
