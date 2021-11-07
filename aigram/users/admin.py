""" Admin Classes"""
# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Models
from aigram.users.models import User
from aigram.users.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin"""
    list_display = ('pk', 'user', 'website', 'picture')
    list_display_links = ('pk', 'user')
    list_editable = ('website', 'picture')

    search_fields = (
        'user__email',
        'user__username',
        'user__first_name',
        'user__last_name',
    )

    list_filter = (
        'user__is_staff',
        'user__is_active',
        'created',
        'modified'
    )

    fieldsets = (
        ('Profile', {
            'fields': (('user', 'picture'),),
        }),
        ('Extra info', {
            'fields': (
                ('website',),
                ('biography',),
            ),
        }),
        ('Metadata', {
            'fields': (('created', 'modified'),),
        }),
    )

    readonly_fields = ('created', 'modified',)


class ProfileInline(admin.StackedInline):
    """ Profile inline admin for user."""

    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'


class UserAdmin(BaseUserAdmin):
    """Add profile admin to base user admin."""
    inlines = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff',
        'is_verified'
    )


#admin.site.unregister(User)
admin.site.register(User, UserAdmin)
