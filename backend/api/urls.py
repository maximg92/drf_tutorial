from django.urls import path

from . import views

# api/ url file.

urlpatterns = [
    path('', views.api_home)

]