from django.urls import path
from django.contrib.auth import views as auth_views
from . import views



urlpatterns=[
    path('home/',views.home,name="home"),
    path('profile/',views.profile,name='profile'),
    path('login/',auth_views.LoginView.as_view(template_name='user/login.html'),name='login'),
    path('register/',views.register,name='register'),
    path('logout/',auth_views.LogoutView.as_view(template_name='user/logout.html'),name='logout')
    # path('update_progress/',views.update_progress,name='update_progress'),
]
