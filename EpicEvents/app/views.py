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
    IsSalesTeam,
    IsSupportTeam,
    IsSalesTeamResponsibleForClient,
    IsSalesTeamResponsibleForContract,
    IsSupportTeamResponsibleForEvent,
)


class UserViewset(ModelViewSet):

    # permission_classes = [IsManagementTeam]
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
        if self.request.method == "GET":
            self.permission_classes = [IsManagementTeam or IsSalesTeam or IsSupportTeam]
        elif self.request.method == "POST":
            self.permission_classes = [IsManagementTeam or IsSalesTeam]
        elif self.request.method == "DELETE":
            self.permission_classes = [IsManagementTeam]
        elif self.request.method == "UPDATE":
            self.permission_classes = [
                IsManagementTeam or IsSalesTeamResponsibleForClient
            ]
        else:
            self.permission_classes = [IsManagementTeam]
        return super(ClientViewset, self).get_permissions()


class ContractViewset(ModelViewSet):

    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    filterset_fields = ["client__last_name", "client__email", "date_created", "amount"]
    search_fields = ["client__last_name", "client__email", "date_created", "amount"]

    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = [IsManagementTeam or IsSalesTeam or IsSupportTeam]
        elif self.request.method == "POST":
            self.permission_classes = [IsManagementTeam or IsSalesTeam]
        elif self.request.method == "DELETE":
            self.permission_classes = [IsManagementTeam]
        elif self.request.method == "UPDATE":
            self.permission_classes = [
                IsManagementTeam or IsSalesTeamResponsibleForContract
            ]
        else:
            self.permission_classes = [IsManagementTeam]
        return super(ContractViewset, self).get_permissions()


class EventViewset(ModelViewSet):

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filterset_fields = ["client__last_name", "client__email", "event_date"]
    search_fields = ["client__last_name", "client__email", "event_date"]

    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = [IsManagementTeam or IsSalesTeam or IsSupportTeam]
        elif self.request.method == "POST":
            self.permission_classes = [IsManagementTeam or IsSalesTeam]
        elif self.request.method == "DELETE":
            self.permission_classes = [IsManagementTeam]
        elif self.request.method == "UPDATE":
            self.permission_classes = [
                IsManagementTeam or IsSupportTeamResponsibleForEvent
            ]
        else:
            self.permission_classes = [IsManagementTeam]
        return super(EventViewset, self).get_permissions()


class Event_StatusViewset(ModelViewSet):

    queryset = Event_Status.objects.all()
    serializer_class = Event_StatusSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = [IsManagementTeam or IsSalesTeam or IsSupportTeam]
        elif self.request.method == "POST":
            self.permission_classes = [IsManagementTeam or IsSalesTeam]
        elif self.request.method == "DELETE":
            self.permission_classes = [IsManagementTeam]
        elif self.request.method == "UPDATE":
            self.permission_classes = [
                IsManagementTeam or IsSupportTeamResponsibleForEvent
            ]
        else:
            self.permission_classes = [IsManagementTeam]
        return super(Event_StatusViewset, self).get_permissions()
