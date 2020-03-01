from django.contrib import admin
from . import models


@admin.register(models.List)
class ListAdmin(admin.ModelAdmin):

    """ List admin defenition """

    list_display = ("user", "name", "count_rooms")

    search_fields = ("name",)

    filter_horizontal = ("rooms",)
