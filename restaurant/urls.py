from django.urls import path, include
from restaurant import views
urlpatterns=[
    path('r/',views.RestaurantView.as_view()),
]