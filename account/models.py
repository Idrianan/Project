from django.db import models
from django.utils import timezone
import datetime
from django.urls import reverse
from django.contrib.auth.models import User


class Forums(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def get_absolute_url(self):
        return reverse('forum:', args=[self.name])

    def __str__(self):
        return self.name


class Themes(models.Model):
    name = models.CharField(max_length=100, unique = True)
    forum_id = models.ForeignKey(Forums, on_delete=models.CASCADE, default=1)
    start_msg_usr_id = models.ForeignKey(User, on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.name


class Post(models.Model):
    msg_text = models.CharField(max_length = 1500)
    theme_id = models.ForeignKey(Themes, on_delete=models.CASCADE,default=1)
    sender_id = models.ForeignKey(User, on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.msg_text
