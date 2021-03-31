from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    print(current_user.id)
    for attr, value in vars(current_user).items():
        print("Attribute: " + str(attr or ""))
        print("Value: " + str(value or ""))
    print(current_user._wrapped.email)
    return render(request, "account/profile.html")
