from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.W

# class User(models.Model):
#     pass


class User(AbstractUser):
    """ Custom User Model """

    avatar = models.ImageField(null=True)
    # 이미지일 경우 Pillow 설치하라 나온다. pipenv install Pillow 로 설치 시도해보고
    # 에러 나오면 버전 부분 문제로 pip로 설치한다.

    gender = models.CharField(max_length=10, null=True)
    # CharField = 한 줄

    # bio = models.TextField(null=True)
    bio = models.TextField(default="")
    # TextField = 여러 줄
