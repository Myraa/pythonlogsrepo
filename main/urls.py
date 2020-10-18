from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from django.contrib.auth import login

urlpatterns = [

    url(r'^$', views.login),
    url('logout', views.logout_view, name='logout'),
    url('home', views.home, name=" "),
    #url(r'^$', login, name='login'),


]
