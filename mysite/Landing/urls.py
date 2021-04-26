from django.urls import path

from . import views
app_name = 'Landing'
urlpatterns = [
    path('profile', views.profile, name='profile'),
    path('', views.go, name='go'),
    path('test', views.test, name="test")
]