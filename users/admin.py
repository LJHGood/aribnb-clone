from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    """ Custom User Admin """

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),  # <- 이 쉼표 해줘야함. 안하면 에러
    )


# @admin.register(models.User)
# class CustomUserAdmin(admin.ModelAdmin):
#     """ Custom User Admin """

#     #
#     list_display = (
#         "username",
#         "email",
#         "gender",
#         "language",
#         "currency",
#         "superhost",
#     )

#     # 필터 도구
#     list_filter = ("language", "currency", "superhost")


# admin.site.register(models.User, CustomUserAdmin)