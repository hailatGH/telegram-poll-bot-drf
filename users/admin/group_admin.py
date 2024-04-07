from django.contrib import admin
from django.contrib.auth.models import Group
from django.utils.html import format_html_join

from users.models import CustomGroup

admin.site.unregister(Group)

class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'display_permissions', 'created_at', 'updated_at')
    search_fields = ('name', 'permissions')
    list_filter = ('created_at', 'updated_at')

    def display_permissions(self, obj):
        return format_html_join(
            ', ',
            '{}',
            ((permission.name,) for permission in obj.permissions.all())
        )

    display_permissions.short_description = 'Permissions'

admin.site.register(CustomGroup, GroupAdmin)
