from urllib.parse import urljoin
from django import urls
from django.urls import path
import urllib3

from .import views
from django.contrib.auth.views import  LogoutView
urlpatterns = [
    path('', views.home,name='home' ),
    path('add/', views.add_show, name="addshow"),
    path('login/', views.MyloginView.as_view(),name='login' ),
    path('logout/', LogoutView.as_view(next_page='login'),name='logout' ),
    path('delete/<int:id>/', views.delete_data, name="deletedata"),
    path(r'profile/(?P<username>[a-zA-Z0-9]+)$', views.get_user_profile)
    
]
