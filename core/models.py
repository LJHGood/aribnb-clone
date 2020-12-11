from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):
    """ Time stamped Model """

    # auto_now_add 모델을 만들면 현재 날짜랑 시간이 여기에 입력
    created = models.DateTimeField(auto_now_add=True)
    # auto_now 내가 모델을 저장할 때마다 매번 새로운 날짜를 입력
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        # abstract 는 데이터 베이스에 등록되지 않는다.