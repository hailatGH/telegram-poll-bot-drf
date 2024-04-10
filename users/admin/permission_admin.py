from django.contrib import admin
from django.contrib.auth.models import Permission

class PermissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'content_type', 'codename')
    search_fields = ('name', 'codename')
    list_filter = ('content_type__app_label', 'content_type__model')

admin.site.register(Permission, PermissionAdmin)

