from django.shortcuts import render

from django.shortcuts import render

def base(request):
    return render(request, 'base.html', {'user': request.user})  # Ensure you have a `base.html` template.


# def home(request):
#     return render(request, 'home.html')


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login  # Alias 'login' as 'auth_login'
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('base')  # Redirect to the home page or another page
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid form data')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

from django.contrib.auth import logout
from django.shortcuts import redirect

def user_logout(request):
    logout(request)
    return redirect('base')  # Redirect to the home page or wherever you want


from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User  # Ensure you have the User model imported

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['confirm_password']

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'OOPS! Username already taken.')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'OOPS! Email already registered.')
            else:
                user = User.objects.create_user(
                    username=username,
                    password=pass1,
                    email=email
                )
                user.save()
                messages.success(request, 'Account created successfully! You can now log in.')
                print("Redirecting to login page")  # Debugging statement
                return redirect('login')  # Ensure 'auth_login' is defined in your URLs
        else:
            messages.error(request, 'Passwords do not match.')

    return render(request, 'signup.html')
def contactus_view(request):
    return render(request, 'contactus.html')  # Contact us page

def getstarted_view(request):
    return render(request, 'getstarted.html')  # Getting started page

def german_view(request):
    return render(request, 'german.html')  # German language page

def french_view(request):
    return render(request, 'french.html')  # French language page

def english_view(request):
    return render(request, 'english.html')  # English language page

def spanish_view(request):
    return render(request, 'spanish.html')  # Spanish language page

def italian_view(request):
    return render(request, 'italian.html')  # Italian language page

def working_view(request):
    return render(request, 'working.html')  # Working page

def chatbot_view(request):
    return render(request, 'chatbot.html')  # Chatbot page

def ga_quiz(request):
    return render(request, 'gaquiz.html')  # A1: Beginner Quiz page

def gb_quiz(request):
    return render(request, 'gbquiz.html')  # A2: Beginner Quiz page

def gc(request):
    return render(request, 'gc.html')  # A1: Intermediate Quiz page

def gd(request):
    return render(request, 'gd.html')  # A2: Intermediate Quiz page

def fa(request):
    return render(request, 'fa.html')  # French A1 Quiz page

def fb(request):
    return render(request, 'fb.html')  # French A2 Quiz page
def fc(request):
    return render(request, 'fc.html')
def fd(request):
    return render(request, 'fd.html')
def sa(request):
    return render(request, 'sa.html')

def sb(request):
    return render(request, 'sb.html')
def sc(request):
    return render(request, 'sc.html')
def sd(request):
    return render(request, 'sd.html')
def ia(request):
    return render(request, 'ia.html')

def ib(request):
    return render(request, 'ib.html')
def ic(request):
    return render(request, 'ic.html')
def id(request):
    return render(request, 'id.html')
def ea(request):
    return render(request, 'ea.html')

def eb(request):
    return render(request, 'eb.html')
def ec(request):
    return render(request, 'ec.html')
def ed(request):
    return render(request, 'ed.html')
