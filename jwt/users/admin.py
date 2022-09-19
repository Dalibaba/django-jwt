from django.contrib import admin
from users.models import User
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea, CharField
from django import forms
from django.db import models


class UserAdminConfig(UserAdmin):
    model = User
    list_filter = ('email',  'is_active', 'is_staff')
    list_display = ('email', 'is_active', 'is_staff')

    ordering = ('-email',)
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 60})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'is_active', 'is_staff')}
         ),
    )


admin.site.register(User, UserAdminConfig)
