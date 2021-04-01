from django.contrib import admin
from .models import CustomUser, video

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(video)