from django.db import models

# Create your models here.
from django.db import models
import datetime
#from django.utils.timezone import utc
from django.utils import timezone


class ControlUtil(models.Model):
    id = models.AutoField(primary_key=True)
    system_id = models.IntegerField()
    control_is_busy = models.BooleanField()


