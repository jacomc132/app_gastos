from django.urls import path
from . import views

app_name='home'

urlpatterns = [
    path('',views.home,name="home"),
    path('login',views.loginPage,name="login"),
    path('logout',views.logoutPage,name="logout"),
    path('register',views.registerPage,name="register"),

]