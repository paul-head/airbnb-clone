from django.db import models
from core import models as core_models


class Review(core_models.TimeStampedModel):

    """ Review model defenition """

    review = models.TextField()
    accuracy = models.IntegerField()
    check_in = models.IntegerField()
    communication = models.IntegerField()
    location = models.IntegerField()
    cleanliness = models.IntegerField()
    value = models.IntegerField()

    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.review} - {self.room}"