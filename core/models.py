from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):

    """ Time Stamped Model """

    created = models.DateTimeField()
    updated - models.DateTimeField()

    class Meta:
        abstract = True  # abstract model은 데이터베이스에 반영되지 않는다.
