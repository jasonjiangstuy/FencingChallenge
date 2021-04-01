from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    print(current_user)
    # print(current_user.id)
    for attr, value in vars(current_user).items():
        print("Attribute: " + str(attr or ""))
        print("Value: " + str(value or ""))
    print(current_user._wrapped.email)
    return render(request, "account/profile.html")

@csrf_exempt
def go(request):
    current_user = request.user

    for key, value in request.POST.items():
        # print('Key: %s' % (key) ) 
        print(f'Key: {key}') in Python >= 3.7
        # print('Value %s' % (value) )
        print(f'Value: {value}') in Python >= 3.7

    # print(current_user.id)
    videoInput = request.POST.get("videoInput", False)
    print(videoInput)
    if (videoInput):
        
        # send to cloud
        pass

    return render(request, "Landing/go.html")
        