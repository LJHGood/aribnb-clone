# django 관련된 내용 전부 import
from django.db import models

# 외부 패키지 import
from django_countries.fields import CountryField

# 내가 만든 패키지 import
from core import models as core_models

# # 객체를 문자로 불러오기 때문에 임폴트 할 필요가 없음.
# from users import models as user_models


# Create your models here.


class AbstractItem(core_models.TimeStampedModel):
    """ Abstract Item """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):
    """ Roomtype Model Definition """

    class Meta:
        verbose_name = "House Type"
        # # 정렬
        # ordering = ["created"]
        # ordering = ["name"]


# Amenity = 예의
class Amenity(AbstractItem):
    """ Amenity Model Definition """

    class Meta:
        # verbose_name_plural = 자세한 이름 복수형
        # verbose = 말 수가 없는
        # plural = 복수형
        verbose_name_plural = "Amenities"


# Facility = 시설
class Facility(AbstractItem):
    """ Facility Model Definition """

    class Meta:
        verbose_name_plural = "Facilities"


# Rule = 규칙
class HouseRule(AbstractItem):
    """ HouseRule Model Dfinition """

    class Meta:
        verbose_name = "House Rule"


class Photo(core_models.TimeStampedModel):
    """ Photo Model Definition """

    caption = models.CharField(max_length=80)
    file = models.ImageField()
    # # Room 수직하강으로 읽기 때문에 Room 객체 찾이 못함.
    # # 이를 해결하기 위해서는 이 함수를 아래로 내리던가
    # # 객체를 문자로 변경하면 됨.
    # room = models.ForeignKey(Room, on_delete=models.CASCADE)

    room = models.ForeignKey("Room", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


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

    # 아래 객체 불러오는 것을 문자로 변경
    # host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    # room_type = models.ForeignKey(RoomType, on_delete=models.SET_NULL, null=True)
    # amenities = models.ManyToManyField(Amenity, blank=True)
    # facilities = models.ManyToManyField(Facility, blank=True)
    # house_rules = models.ManyToManyField(HouseRule, blank=True)

    # user 연결하는 거
    # CASCADE : 폭포수 -> 위에서 아래로 떨어지는 효과
    # 1대 다 관계이니 1이 삭제되면 같이 삭제 되는 것. on_delete=models.CASCADE
    host = models.ForeignKey("users.User", on_delete=models.CASCADE)
    # 아래 내용 core에서 만들었다
    # created = models.DateTimeField()
    # updated = models.DateTimeField()

    # 다 대 다 연결
    # 다중 선택, 추가만 가능
    # room_type = models.ManyToManyField(RoomType, blank=True)

    # 원본 삭제돼도 유지하기 위함
    # 한 사람이 여러 객실 유형을 선택하지 않게 하기 위해서 null=True
    # 단일 선택
    # 추가, 수정, 삭제 가능(on_delete=models.SET_NULL 이걸로인해서)
    room_type = models.ForeignKey("RoomType", on_delete=models.SET_NULL, null=True)

    # 다 대 다 연결
    # 빈칸 허용(blank=True)
    amenities = models.ManyToManyField("Amenity", blank=True)

    facilities = models.ManyToManyField("Facility", blank=True)
    house_rules = models.ManyToManyField("HouseRule", blank=True)

    def __str__(self):
        return self.name
