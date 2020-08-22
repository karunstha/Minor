from django.urls import path, include
from users.views import login_view,signup_view,home_view,logout_view,billing_view,menu_view,tables_view,history_view
from rest_framework.authtoken import views as viewz
urlpatterns = [
    path('',login_view,name='login_view'),
    # path('login/',auth_views.LoginView.as_view(template_name='Login/index.html'),name='login'),
    path('signup/',signup_view,name='signup_view'),
    path('token/',viewz.obtain_auth_token),
    path('home/',home_view,name='home'),
    path('logout/',logout_view,name='logout'),
    path('billing/',billing_view,name='billing'),
    path('menu/',menu_view,name='menu'),
    path('tables/',tables_view,name='tables'),
    path('history/',history_view,name='history'),
]