# chat/views.py
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from .forms import MessageForm, UserRegisterForm
from .models import Chat, Contact, Message


def home(request):
    if not request.user.is_authenticated:
        return redirect('login')

    user_contact = Contact.objects.get(user=request.user)
    chats = Chat.objects.filter(participants=user_contact)
    
    return render(request, 'chat/home.html', {'chats': chats})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Contact.objects.create(user=user)
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'chat/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'chat/login.html', {'error': 'Invalid credentials'})

    return render(request, 'chat/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def chat_view(request, chat_id):
    chat = Chat.objects.get(id=chat_id)
    user_contact = Contact.objects.get(user=request.user)
    
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = user_contact
            message.recipient = chat.participants.exclude(user=request.user).first()
            message.save()
            chat.messages.add(message)
            return redirect('chat_view', chat_id=chat_id)
    
    form = MessageForm()
    return render(request, 'chat/chat.html', {'chat': chat, 'form': form})
