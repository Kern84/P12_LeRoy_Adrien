from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from app.models import User, Client, Contract, Event, Event_Status


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "role",
            "password",
            "date_created",
            "is_superuser",
            "is_staff",
        ]

    def validate_password(self, value):
        return make_password(value)


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "phone",
            "mobile",
            "compagny_name",
            "sale_contact",
            "actual_client",
        ]


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ["id", "sale_contact", "client", "status", "amount", "payment_due"]


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            "id",
            "client",
            "support_contact",
            "event_status",
            "attendees",
            "event_date",
            "notes",
        ]


class Event_StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event_Status
        fields = ["id", "status"]
