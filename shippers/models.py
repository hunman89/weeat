from django.db import models
from core import models as core_models


class Shipper(core_models.TimeStampedModel):

    """ Account model definition"""

    name = models.CharField(max_length=80)
    location = models.IntegerField()
