from . import views
from django.urls import path

urlpatterns = [

    path('',views.index,name='index'),
    path('home', views.home, name='home'),
    path('details', views.details, name='details'),
    path('ajax/load-courses/', views.load_courses, name='ajax_load_courses'),
    path('order', views.order, name='order'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('computer',views.computer,name='computer'),
    path('commerce',views.commerce,name='commerce'),
    path('maths',views.maths,name='maths'),
    path('science',views.science,name='science'),
]