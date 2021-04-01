from django.urls import path

from . import views
app_name = 'Landing'
urlpatterns = [
    path('', views.index, name='index'),
    path('profile', views.profile, name='profile'),
    path('go', views.go, name='go'),
]