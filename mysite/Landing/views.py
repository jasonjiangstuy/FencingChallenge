from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.apps import apps
# MyModel1 = apps.get_model('users', 'video')
from .forms import VideoForm


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

challenges = apps.get_model('users', 'challenge')
@csrf_exempt
def go(request):

    form= VideoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        prep = form.save(commit=False)
        prep.author = request.user
        prep.save()
        return render(request, "Landing/success.html")

    current_user = request.user

    challenge_list = challenges.objects.all()
    for challenge in challenge_list:
        print(challenge.name)
    context = {
        "form":form,
        "challengeList":challenge_list,
    }
    return render(request, "Landing/go.html", context)
        