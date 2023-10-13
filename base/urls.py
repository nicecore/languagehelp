from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('<str:username>/<str:pk>/', views.post, name="post"),
    path('profile/<int:pk>', views.profile, name='profile'),
    path('create-post/', views.createPost, name="create-post"),
    path('delete-post/<str:pk>', views.deletePost, name="delete-post"),
    path('delete-reply/<str:pk>', views.deleteReply, name="delete-reply"),
    path('language/<str:pk>', views.language_profile, name="language-profile"),
]