# django 관련된 내용 전부 import
from django.db import models

# 외부 패키지 import
from django_countries.fields import CountryField

# 내가 만든 패키지 import
from core import models as core_models
from users import models as user_models


# Create your models here.


class AbstractItem(core_models.TimeStampedModel):
    """ Abstract Item """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):
    pass


class Room(core_models.TimeStampedModel):
    """ Room Model Definition """

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    # user 연결하는 거
    host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    # 아래 내용 core에서 만들었다
    # created = models.DateTimeField()
    # updated = models.DateTimeField()

    # 다 대 다 연결
    room_type = models.ManyToManyField(RoomType, blank=True)

    def __str__(self):
        return self.name
