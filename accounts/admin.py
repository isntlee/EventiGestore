from django.contrib import admin
from . import models


class UserAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (("Personal info"), {"fields": ("email",)}),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (("Dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ["username", "id", "is_superuser", "slug"]
    search_fields = ["username"]

admin.site.register(models.User, UserAdmin)