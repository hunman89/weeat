from django.db import models
from core import models as core_models


class Account(core_models.TimeStampedModel):

    """ Account model definition"""

    name = models.CharField(max_length=80)

    foods = models.ManyToManyField("foods.Food", related_name="accounts")
    stock = models.CharField(max_length=40)
