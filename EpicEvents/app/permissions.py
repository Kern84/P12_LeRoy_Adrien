from rest_framework.permissions import BasePermission

from app.models import Client, Contract, Event


class IsManagementTeam(BasePermission):
    def has_permission(self, request, view):
        if (
            request.user.is_authenticated
            and request.user.is_superuser
            and request.user.role == "Management"
        ):
            return True
        else:
            return False


class IsInTeam(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.is_superuser and request.user.role == "Management":
                return True
            elif request.user.role == "Sales":
                return True
            elif request.user.role == "Support":
                return True
            else:
                return False
        else:
            return False


class IsSalesTeamOrManagement(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.is_superuser and request.user.role == "Management":
                return True
            elif request.user.role == "Sales":
                return True
            else:
                return False
        else:
            return False


class IsSalesTeamResponsibleForClientOrManagement(BasePermission):
    def has_permission(self, request, view):
        user_id = request.user.id
        if request.user.is_authenticated:
            if request.user.is_superuser and request.user.role == "Management":
                return True
            else:
                if request.user.role == "Sales":
                    client_id = int(request.resolver_match.kwargs["pk"])
                    client = Client.objects.get(pk=client_id)
                    if client.sale_contact_id == user_id:
                        return True
                    else:
                        return False
                else:
                    return False
        else:
            return False


class IsSalesTeamResponsibleForContractOrManagement(BasePermission):
    def has_permission(self, request, view):
        user_id = request.user.id
        if request.user.is_authenticated:
            if request.user.is_superuser and request.user.role == "Management":
                return True
            else:
                if request.user.role == "Sales":
                    contract_id = int(request.resolver_match.kwargs["pk"])
                    contract = Contract.objects.get(pk=contract_id)
                    if contract.sale_contact_id == user_id:
                        return True
                    else:
                        return False
                else:
                    return False
        else:
            return False


class IsSupportTeamResponsibleForEventOrManagement(BasePermission):
    def has_permission(self, request, view):
        user_id = request.user.id
        if request.user.is_authenticated:
            if request.user.is_superuser and request.user.role == "Management":
                return True
            else:
                if request.user.role == "Support":
                    event_id = int(request.resolver_match.kwargs["pk"])
                    event = Event.objects.get(pk=event_id)
                    if event.support_contact_id == user_id:
                        return True
                    else:
                        return False
                else:
                    return False
        else:
            return False
