from django.urls import path

from . import views

app_name = 'VidFetch'
urlpatterns = [
    path('', views.download_video, name='download_video'),
]
