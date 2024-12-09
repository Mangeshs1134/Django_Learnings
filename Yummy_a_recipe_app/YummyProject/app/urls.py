
from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # path('', views.home , name='home'),
    path('', views.recipe_list , name='list'),
    path('oldest/', views.oldest , name='oldest'),
    path('recipe/create/', views.recipe_create , name='recipe_create'),
    path('<int:recipe_id>/edit/', views.recipe_edit , name='recipe_edit'),
    path('<int:recipe_id>/delete/', views.recipe_delete , name='recipe_delete'),
    path('<int:recipe_id>/like/', views.like_others_post , name='like_others_post'),
    path('register/', views.register , name='register'),
    path('search/', views.search , name='search'),

]