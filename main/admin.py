from csv import list_dialects
from django.contrib import admin
from main.models import *
from django.utils.safestring import mark_safe
from django.conf import settings
from datetime import datetime
from django.contrib.auth.models import User, Group

admin.site.site_header = 'Панель администратора'


class RoomsImageAdmin(admin.StackedInline):
    model = RoomsImages


class RoomsCostAdmin(admin.StackedInline):
    model = RoomsCost


class RoomsDevicesAdmin(admin.StackedInline):
    model = RoomsDevices


class RoomsAccessoriesAdmin(admin.StackedInline):
    model = RoomsAccessories


@admin.register(Rooms)
class RoomsAdmin(admin.ModelAdmin):
    inlines = [RoomsImageAdmin, RoomsCostAdmin,
               RoomsDevicesAdmin, RoomsAccessoriesAdmin]

    class Meta:
        model = Rooms


class SiteRulesAdmin(admin.StackedInline):
    model = SiteRules


class SiteContactsAdmin(admin.StackedInline):
    model = SiteContacts

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):

    inlines = [SiteContactsAdmin, SiteRulesAdmin]

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'date')
    readonly_fields = ('name', 'number', 'date')

    def has_add_permission(self, request, obj=None):
        return False


admin.site.unregister(Group)
admin.site.unregister(User)

