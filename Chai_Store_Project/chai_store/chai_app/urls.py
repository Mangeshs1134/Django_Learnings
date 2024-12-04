from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    # path("" , views.home , name="chai_app_home"),
    path("" , views.display_stores , name="display_stores"),
    path("<int:chai_id>" , views.chai_detail , name="chai_detail"),
    
]