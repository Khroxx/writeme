from django.db import models
from django.conf import settings
from django.db.models.fields import DateField
from datetime import date

# Create your models here.

class Message(models.Model):
    text = models.CharField(max_length=500)
    created_at = DateField(default=date.today)
    # chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author_message_set')
    reciever = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reciever_message_set')