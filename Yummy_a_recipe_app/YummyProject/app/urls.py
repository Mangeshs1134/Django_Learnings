
from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # path('', views.home , name='home'),
    path('', views.recipe_list , name='list'),
    path('oldest/', views.oldest , name='oldest'),
    path('popular/', views.popular , name='popular'),
    path('sweet/', views.sweet , name='sweet'),
    path('punjabi/', views.punjabi , name='punjabi'),
    path('indo_chinease/', views.indo_chinease , name='indo_chinease'),
    path('spicy/', views.spicy , name='spicy'),
    path('up_special/', views.up_special , name='up_special'),
    path('recipe/create/', views.recipe_create , name='recipe_create'),
    path('<int:recipe_id>/edit/', views.recipe_edit , name='recipe_edit'),
    path('<int:recipe_id>/view_recipe/', views.view_recipe , name='view_recipe'),
    path('<int:recipe_id>/delete/', views.recipe_delete , name='recipe_delete'),
    path('<int:recipe_id>/like/', views.like_others_post , name='like_others_post'),
    path('register/', views.register , name='register'),
    path('search/', views.search , name='search'),

]