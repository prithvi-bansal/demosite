from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.UserLogin.as_view(), name='login'),
    path('register/', views.UserSignup.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]