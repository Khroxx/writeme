from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from .models import Chat, Message
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

# Leitet zu login.html solange man ausgeloggt ist
@login_required(login_url='/login/')

# Zeigt chat(index.html) an
def index(request):
    if request.method == 'POST':
        print('Recived Data ' + request.POST['textmessage'])
        myChat = Chat.objects.get(id=1)
        new_message = Message.objects.create(text=request.POST['textmessage'], chat=myChat, author=request.user, reciever=request.user)
        # message in JSON umwandeln und an Frontend geben
        serialized_message = serializers.serialize('json', [new_message])
        return JsonResponse(serialized_message[1:-1], safe=False)
    chatMessages = Message.objects.filter(chat__id=1)
    return render(request, 'chat/index.html', {'messages': chatMessages})

# Zeigt login.html an
def login_view(request):
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
    logout(request)
    return HttpResponseRedirect('/login/')