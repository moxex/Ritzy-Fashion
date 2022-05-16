from django.urls import path
from . import views

app_name = 'mart'

urlpatterns = [
    path('', views.home, name='rizzy-home'),
]