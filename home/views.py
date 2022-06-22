from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def counting(request):
    return render(request, 'counting.html', {"test": "Counting"})


def usercounting(request):
    return render(request, 'usercounting.html', {"test": "User Counting"})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'signup.html', {"test": "Signup"})
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {"form": form})


def banner(request):
    return render(request, 'banner.html')