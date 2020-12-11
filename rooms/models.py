from django.db import models
from django_countries.fields import CountryField
from core import models as core_models

# Create your models here.


class Room(core_models.TimeStampedModel):
    """ Room Model Definition """

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()

    # 아래 내용 core에서 만들었다
    # created = models.DateTimeField()
    # updated = models.DateTimeField()
    # rooms가 만들어질 때나 업데이트될 때를 알수있으면