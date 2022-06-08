from rest_framework.permissions import BasePermission

from app.models import Client, Contract, Event


class IsManagementTeam(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user.is_authenticated
            and request.user.is_superuser
            and request.user.role == "Management"
        )


class IsSalesTeam(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and request.user.role == "Sales")


class IsSalesTeamResponsibleForClient(BasePermission):
    def has_permission(self, request, view):
        user_id = request.user.id
        if request.user.is_authenticated:
            if request.user.role == "Sales":
                if request.resolver_match.kwargs:
                    try:
                        client_id = int(request.resolver_match.kwargs["client_pk"])
                    except KeyError:
                        client_id = int(request.resolver_match.kwargs["pk"])
                    client = Client.objects.get(pk=client_id)
                    if client.sale_contact_id.id == user_id:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False


class IsSalesTeamResponsibleForContract(BasePermission):
    def has_permission(self, request, view):
        user_id = request.user.id
        if request.user.is_authenticated:
            if request.user.role == "Sales":
                if request.resolver_match.kwargs:
                    try:
                        contract_id = int(request.resolver_match.kwargs["contract_pk"])
                    except KeyError:
                        contract_id = int(request.resolver_match.kwargs["pk"])
                    contract = Contract.objects.get(pk=contract_id)
                    if contract.sale_contact_id.id == user_id:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False


class IsSupportTeam(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and request.user.role == "Support")


class IsSupportTeamResponsibleForEvent(BasePermission):
    def has_permission(self, request, view):
        user_id = request.user.id
        if request.user.is_authenticated:
            if request.user.role == "Support":
                if request.resolver_match.kwargs:
                    try:
                        event_id = int(request.resolver_match.kwargs["event_pk"])
                    except KeyError:
                        event_id = int(request.resolver_match.kwargs["pk"])
                    event = Event.objects.get(pk=event_id)
                    if event.support_contact_id.id == user_id:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
