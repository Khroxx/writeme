from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import render, redirect
from django.http.response import HttpResponseRedirect
from .models import Chat, Message
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import json

# Create your views here.

# if not logged in, redirect to login page
@login_required(login_url='/login/')

def index(request):
    """
    renders chat/index.html and handles POST requests for messages
    """
    if request.method == 'POST':
        myChat = Chat.objects.get(id=1)
        new_message = Message.objects.create(text=request.POST['textmessage'], chat=myChat, author=request.user, reciever=request.user)
        # message in JSON umwandeln und an Frontend geben
        serialized_message = serializers.serialize('json', [new_message, ])
        message_data = json.loads(serialized_message)[0]
        message_data['fields']['author'] = request.user.username  
        message_data['fields']['created_at'] = new_message.created_at.strftime('%B %d, %Y')
        return JsonResponse(message_data, safe=False)
    chatMessages = Message.objects.filter(chat__id=1)
    return render(request, 'chat/index.html', {'messages': chatMessages})

def login_view(request): 
    """
    renders login.html and handles POST requests for login
    """
    redirect = request.GET.get('next', '/chat/')
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user:
            login(request, user)
            return HttpResponseRedirect(request.POST.get('redirect'))
        else:
            return render(request, 'auth/login.html', {'wrongPassword': True, 'redirect': redirect})

    return render(request, 'auth/login.html', { 'redirect': redirect })


# Zeigt register.html an
def register_view(request):
    """
    renders register.html and handles POST requests for registration
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_again = request.POST.get('password-again')
        
        if User.objects.filter(username=username).exists():
            print(username)
            return render(request, 'auth/register.html', {'usernameExists': True})
        if password != password_again:
            return render(request, 'auth/register.html', {'passwordsNotEqual': True})
        else:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return HttpResponseRedirect('/login/')
    return render(request, 'auth/register.html')

def logout_view(request):
    """
    logs out the user and redirects to login
    """
    logout(request)
    return HttpResponseRedirect('/login/')

def redirect_login(request):
    """
    redirects to login from blank url
    """
    return redirect('/login/')