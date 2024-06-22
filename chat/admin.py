from django.contrib import admin
from .models import Chat, Message

# Backend Models mit Anzeigereiter
class MessageAdmin(admin.ModelAdmin):
    field = ('chat', 'text', 'created_at', 'author', 'reciever')
    list_display = ('text', 'chat', 'author', 'reciever', 'created_at')
    search_fields = ('text', 'author')
    pass

class ChatAdmin(admin.ModelAdmin):
    field = ('created_at',)
    list_display = ('created_at',)
    pass


# Register your models here.

admin.site.register(Message, MessageAdmin)
admin.site.register(Chat, ChatAdmin)