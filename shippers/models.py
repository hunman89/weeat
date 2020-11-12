from django.db import models
from core import models as core_models


class Shipper(core_models.TimeStampedModel):
    name = models.CharField()
    location = models.IntegerField()
