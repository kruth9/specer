from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('<int:id>',views.Blogdetails,name="blogdetails"),
    path('',views.index,name="index"),
    path('Home',views.Home,name="Home"),
    path('blog/',views.Handle_Blog,name="blog"),
    path('contact/',views.Contact,name="contact"),
    path('results/',views.Result,name="results"),
    path('schedule/',views.Schedule,name="schedule"),
    path('clubs/',views.Club,name="clubs"),
    path('signup/',views.Handle_Register,name="signup"),
    path('signin/',views.Handle_Signin,name="signin"),
    path('logout', views.Handle_logout, name='logout'),
    path('search/', views.SearchFunction, name='search'),
   
    
]