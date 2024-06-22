from django.db import models
from django.conf import settings
from datetime import date

# Create your models here.

# Chat Model im Backend adminbereich
class Chat(models.Model):
    created_at = models.DateField(default=date.today)

# Message Model im Backend adminbereich
class Message(models.Model):
    text = models.CharField(max_length=500)
    created_at = models.DateField(default=date.today)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='chat_message_set', default=None, blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author_message_set')
    reciever = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reciever_message_set')


