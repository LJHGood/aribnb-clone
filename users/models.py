from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.W

# class User(models.Model):
#     pass


class User(AbstractUser):
    """ Custom User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"

    LANGUAGE_CHOICES = ((LANGUAGE_ENGLISH, "English"), (LANGUAGE_KOREAN, "Korean"))

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = ((CURRENCY_USD, "USD"), (CURRENCY_KRW, "KRW"))

    avatar = models.ImageField(null=True, blank=True)
    # 이미지일 경우 Pillow 설치하라 나온다. pipenv install Pillow 로 설치 시도해보고
    # 에러 나오면 버전 부분 문제로 pip로 설치한다.

    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=10, null=True, blank=True
    )
    # CharField = 한 줄
    # choices=GENDER_CHOICES 추가로 선택하는 폼으로 변경됐다.
    # 이 때 데이터베이스에 직접적인 영향을 주지 않는다.

    # bio = models.TextField(null=True)
    bio = models.TextField(default="", blank=True)
    # TextField = 여러 줄

    # blank=True는 선택.

    birthdate = models.DateField(null=True)

    langauge = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=2, null=True, blank=True
    )

    currency = models.CharField(
        choices=CURRENCY_CHOICES, max_length=3, null=True, blank=True
    )

    # 슈퍼 호스트 추가.(슈퍼 권한)
    superhost = models.BooleanField(default=False)