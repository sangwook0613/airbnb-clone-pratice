from django.db import models  # 먼저 장고를 받고
from django_countries.fields import CountryField  # 그 다음 외부패키지
from core import models as core_models  # 마지막으로 내가 만든 패키지
from users import models as user_models

# Create your models here.
class Room(core_models.TimeStampedModel):

    """ Room Model Defintion """

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    guests = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
