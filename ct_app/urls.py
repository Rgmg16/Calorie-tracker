from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('food_list/', views.food_list, name='food_list'),
    path('delete_food/<int:food_id>/', views.delete_food, name='delete_food'),
    path('reset_calories/', views.reset_calories, name='reset_calories'),
]
