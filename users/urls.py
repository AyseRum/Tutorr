from django.urls import path, include
import homepage.views
from . import views


urlpatterns = [
    path('', homepage.views.homepage),
    path('register', views.register, name='register'),
]
