from rest_framework.viewsets import ModelViewSet

from app.models import User, Client, Contract, Event, Event_Status
from app.serializers import (
    UserSerializer,
    ClientSerializer,
    ContractSerializer,
    EventSerializer,
    Event_StatusSerializer,
)
from app.permissions import (
    IsManagementTeam,
    IsInTeam,
    IsSalesTeamOrManagement,
    IsSalesTeamResponsibleForClientOrManagement,
    IsSalesTeamResponsibleForContractOrManagement,
    IsSupportTeamResponsibleForEventOrManagement,
)


class UserViewset(ModelViewSet):

    permission_classes = [IsManagementTeam]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_fields = ["last_name", "role"]
    search_fields = ["last_name", "role"]


class ClientViewset(ModelViewSet):

    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filterset_fields = ["last_name", "email"]
    search_fields = ["last_name", "email"]

    def get_permissions(self):
        permission_classes = []
        if self.request.method == "GET":
            permission_classes = [IsInTeam()]
        elif self.request.method == "POST":
            permission_classes = [IsSalesTeamOrManagement()]
        elif self.request.method == "DELETE":
            permission_classes = [IsManagementTeam()]
        elif self.request.method == "PUT":
            permission_classes = [
                IsSalesTeamResponsibleForClientOrManagement(),
            ]
        else:
            permission_classes = [IsManagementTeam()]
        return permission_classes


class ContractViewset(ModelViewSet):

    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    filterset_fields = ["client__last_name", "client__email", "date_created", "amount"]
    search_fields = ["client__last_name", "client__email", "date_created", "amount"]

    def get_permissions(self):
        permission_classes = []
        if self.request.method == "GET":
            permission_classes = [IsInTeam()]
        elif self.request.method == "POST":
            permission_classes = [IsSalesTeamOrManagement()]
        elif self.request.method == "DELETE":
            permission_classes = [IsManagementTeam()]
        elif self.request.method == "PUT":
            permission_classes = [
                IsSalesTeamResponsibleForContractOrManagement(),
            ]
        else:
            permission_classes = [IsManagementTeam()]
        return permission_classes


class EventViewset(ModelViewSet):

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filterset_fields = ["client__last_name", "client__email", "event_date"]
    search_fields = ["client__last_name", "client__email", "event_date"]

    def get_permissions(self):
        permission_classes = []
        if self.request.method == "GET":
            permission_classes = [IsInTeam()]
        elif self.request.method == "POST":
            permission_classes = [IsSalesTeamOrManagement()]
        elif self.request.method == "DELETE":
            permission_classes = [IsManagementTeam()]
        elif self.request.method == "PUT":
            permission_classes = [
                IsSupportTeamResponsibleForEventOrManagement(),
            ]
        else:
            permission_classes = [IsManagementTeam()]
        return permission_classes


class Event_StatusViewset(ModelViewSet):

    queryset = Event_Status.objects.all()
    serializer_class = Event_StatusSerializer

    def get_permissions(self):
        permission_classes = []
        if self.request.method == "GET":
            permission_classes = [IsInTeam()]
        elif self.request.method == "POST":
            permission_classes = [IsSalesTeamOrManagement()]
        elif self.request.method == "DELETE":
            permission_classes = [IsManagementTeam()]
        elif self.request.method == "PUT":
            permission_classes = [
                IsSupportTeamResponsibleForEventOrManagement(),
            ]
        else:
            permission_classes = [IsManagementTeam()]
        return permission_classes
