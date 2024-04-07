from django.contrib import admin
from django.utils.html import format_html

from users.models import CustomUser

class UserAdmin(admin.ModelAdmin):
    list_display = ('display_profile_image','username', 'first_name', 'last_name', 'email', 'email_verified', 'phone_number', 'is_staff', 'is_active', 'is_superuser', 'display_groups', 'display_permissions', 'last_login', 'created_at', 'updated_at')
    search_fields = ('username', 'first_name', 'last_name', 'email', 'phone_number')
    list_filter = ('is_staff', 'is_active', 'is_superuser', 'last_login', 'created_at', 'updated_at')

    def display_profile_image(self, obj):
        if obj.profile_image:
            return format_html('<img src="{}" style="max-height: 40px; max-width: 40px; border-radius: 8px" />', obj.profile_image.url)
        else:
            return format_html('<img src="{}" style="max-height: 40px; max-width: 40px; border-radius: 8px" />', '/media/users_profile_images/default.jpg')
            return 'No Image'
        
    def display_permissions(self, obj):
        permissions = ', '.join([permission.name for permission in obj.user_permissions.all()])
        return permissions if permissions else '-'
    
    def display_groups(self, obj):
        groups = ', '.join([group.name for group in obj.groups.all()])
        return groups if groups else '-'

    display_groups.short_description = 'Groups'
    display_permissions.short_description = 'Permissions'
    display_profile_image.short_description = 'Profile Image' 

admin.site.register(CustomUser, UserAdmin)