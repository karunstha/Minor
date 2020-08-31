from django.urls import path, include
from fooditem import views
urlpatterns=[
    path('food/',views.FoodItemView.as_view()),
    path('food/<int:pk>/',views.FoodItemView.as_view()),
]