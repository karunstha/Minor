from django.urls import path, include
from orders import views
urlpatterns=[
    path('o/',views.OrderView.as_view()),
    path('o/<int:pk>/',views.OrderView.as_view()),
    path('oi/',views.OrderItemView.as_view()),
    path('oi/<int:pk>/',views.OrderItemView.as_view()),
    
]