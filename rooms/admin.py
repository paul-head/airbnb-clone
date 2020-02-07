from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """ Item ADmin DEfenition """

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin DEfenition """

    fieldsets = (
        ("Basic Info", {"fields": ("name", "description", "country", "price")}),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
        (
            "More About the space",
            {
                "classes": ("collapse",),
                "fields": ("amenities", "facilities", "house_rule"),
            },
        ),
        ("Spaces", {"fields": ("guests", "beds", "bedrooms", "baths")}),
        ("Last Details", {"fields": ("host",)}),
    )

    list_display = (
        "name",
        # "description",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
    )

    list_filter = (
        "instant_book",
        "host__superhost",
        "room_type",
        "amenities",
        "facilities",
        "house_rule",
        "city",
        "country",
    )

    search_fields = ("city", "^host__username")

    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rule",
    )


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """  """

    pass
