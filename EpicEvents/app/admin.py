from django.contrib import admin
from app.models import User, Client, Contract, Event, Event_Status


class UserAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "role")
    list_filter = ("last_name", "role")
    search_fields = ("last_name", "role")


class ClientAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "compagny_name", "actual_client")
    list_filter = ("last_name", "email")
    search_fields = ("last_name", "email")


class ContractAdmin(admin.ModelAdmin):
    list_display = ("id", "sale_contact", "client")
    list_filter = ("client", "date_created", "amount")
    search_fields = ("client", "date_created", "amount")


class EventAdmin(admin.ModelAdmin):
    list_display = ("id", "support_contact", "client", "event_status")
    list_filter = (
        "client",
        "event_date",
    )
    search_fields = ("client", "event_date")


class EventStatusAdmin(admin.ModelAdmin):
    list_display = ("status",)
    list_filter = ("status",)
    search_fields = ("status",)


admin.site.register(User, UserAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Contract, ContractAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Event_Status, EventStatusAdmin)
