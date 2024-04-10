from django.contrib import admin
from django.contrib.auth.models import Group
from django.utils.html import format_html_join

admin.site.unregister(Group)

class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_permissions')
    search_fields = ('name', 'permissions')

    def display_permissions(self, obj):
        return format_html_join(
            ', ',
            '{}',
            ((permission.name,) for permission in obj.permissions.all())
        )

    display_permissions.short_description = 'Permissions'

admin.site.register(Group, GroupAdmin)
