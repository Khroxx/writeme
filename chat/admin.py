from django.contrib import admin
from .models import Message

class MessageAdmin(admin.ModelAdmin):
    field = ('text', 'created_at', 'author', 'reciever')
    list_display = ('text', 'author', 'reciever', 'created_at')
    search_fields = ('text', 'author')
    pass
# Register your models here.

admin.site.register(Message, MessageAdmin)