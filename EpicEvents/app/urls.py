from rest_framework import routers

from app.views import (
    UserViewset,
    ClientViewset,
    ContractViewset,
    EventViewset,
    Event_StatusViewset,
)


router = routers.SimpleRouter()
router.register("user", UserViewset, basename="user")
router.register("client", ClientViewset, basename="client")
router.register("contract", ContractViewset, basename="contract")
router.register("event", EventViewset, basename="event")
router.register("event_status", Event_StatusViewset, basename="event_status")
