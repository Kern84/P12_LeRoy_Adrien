from django import forms
from django.apps import apps
from app.models import User, Contract, Client


class UserForm(forms.ModelForm):
    """Form to create a user."""

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "role",
            "password",
            "is_superuser",
            "is_staff",
        ]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class ContractForm(forms.ModelForm):
    """Form to create a contract."""

    class Meta:
        model = Contract
        fields = ["sale_contact", "client", "status", "amount", "payment_due"]

    def save(self, commit=True):
        contract = super().save(commit=False)
        related_client = Client.objects.get(id=contract.client.id)
        event = apps.get_model("app", "Event")
        new_event = event.objects.create(client=related_client)
        new_event.save()
        if commit:
            contract.save()
        return contract
