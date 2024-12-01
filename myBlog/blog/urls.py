from django.urls import path
from .views import PostView, PostDetailView, register, login_view, profile_view
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', PostView.as_view(), name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('profile/', profile_view, name='profile'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
]
