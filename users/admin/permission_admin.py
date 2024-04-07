from django.contrib import admin

from users.models import CustomPermission

class PermissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'content_type', 'codename', 'created_at', 'updated_at')
    search_fields = ('name', 'codename')
    list_filter = ('content_type__app_label', 'content_type__model', 'created_at', 'updated_at')

admin.site.register(CustomPermission, PermissionAdmin)

