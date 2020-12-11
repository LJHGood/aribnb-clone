from django.db import models
from core import models as core_models

# Create your models here.


class Room(core_models.TimeStampedModel):
    """ Room Model Definition """

    pass

    # 아래 내용 core에서 만들었다

    # created = models.DateTimeField()
    # updated = models.DateTimeField()
    # rooms가 만들어질 때나 업데이트될 때를 알수있으면