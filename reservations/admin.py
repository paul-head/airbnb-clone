from django.contrib import admin
from . import models


@admin.register(models.Reservetion)
class ReservationAdmin(admin.ModelAdmin):

    """ Reservation Admin Definition """

    pass
