from django.db import models
from core import models as core_models


class Food(core_models.TimeStampedModel):

    """ Food model definition"""

    name = models.CharField(max_length=80)
