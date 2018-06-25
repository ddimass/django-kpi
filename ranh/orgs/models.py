from django.db import models
from django.conf import settings

# Create your models here.

class Org(models.Model):
    name = models.CharField(verbose_name="Название организации", max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
