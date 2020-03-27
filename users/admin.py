from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.User)  # decorator는 바로 위에 있어야함(공백없이)
class CustomUserAdmin(admin.ModelAdmin):

    """ Custom User Admin """

    list_display = ("username", "email", "gender", "language", "currency", "superhost")
    list_filter = ("language", "currency", "superhost")
