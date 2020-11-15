from django.db import models
from core import models as core_models


class Order(core_models.TimeStampedModel):

    """ Order model definition"""

    user = models.ForeignKey("users.User", related_name="orders")
    foods = models.ManyToManyField("foods.Food", related_name="orders")
