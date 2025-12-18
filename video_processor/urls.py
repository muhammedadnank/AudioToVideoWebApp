from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_video, name='upload_video'),
]
