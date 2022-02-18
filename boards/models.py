from django.db import models
from django.utils import timezone
import datetime

class Board(models.Model):
    name = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    created_by = models.CharField(max_length=30)
    def __str__(self):
        return self.name
# Create your models here.
