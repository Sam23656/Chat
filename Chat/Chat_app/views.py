from django.shortcuts import render, redirect
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import CreateView
from django.contrib.auth.models import User

from Chat_app.forms import MessageModelForm
from Chat_app.models import Message

# Create your views here.

from django.db.models import Q


def show_index_page(request):
    context = {}
    bot_user = User.objects.get_by_natural_key('Bot')
    if request.user.is_authenticated:
        user_messages = Message.objects.filter(
            Q(author=request.user, recipient=bot_user) | Q(author=bot_user, recipient=request.user)
        ).order_by('date')
        context = {'messages': user_messages, 'form': MessageModelForm()}

    if request.method == 'POST':
        text = request.POST.get('text')
        author = request.user
        recipient = bot_user
        Message.objects.create(text=text, author=author, recipient=recipient)
        Message.objects.create(text=text, author=bot_user, recipient=author)
        return redirect('index')

    return render(request, 'Chat_app/index.html', context=context)


class LogOutViewPage(LogoutView):
    next_page = reverse_lazy("index")


class RegisterViewPage(CreateView):
    template_name = "Chat_app/register.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("index")


class LoginViewPage(LoginView):
    template_name = "Chat_app/login.html"
    form_class = AuthenticationForm
    next_page = reverse_lazy("index")
