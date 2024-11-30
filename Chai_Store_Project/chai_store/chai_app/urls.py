from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path("" , views.home , name="chai_app_home"),
    
]