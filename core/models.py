from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):
    """ Time stamped Model """

    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        abstract = True
        # abstract 는 데이터 베이스에 등록되지 않는다.