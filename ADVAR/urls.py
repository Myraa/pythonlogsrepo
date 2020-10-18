"""testcase_automation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from main import views
from django.contrib.auth import login,logout
from GIDP import urls as gidp


from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views


urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url('ADVAR/', include('django.contrib.auth.urls')),
    url(r'^ADVAR/', include('main.urls')),
    #url(r'^login/$', login, name='login'),

    url(r'^GIDP/', include('GIDP.urls')),
    # url(r'^GIDP/Reports/$', gidp.reports, name='reports6'),
    # url(r'^GIDP/Filter$', gidp.filter, name='rep'),


    url(r'^ADVAR/login/$', login, name='login'),
    url(r'^ADVAR/logout/$', logout, name='logout'),
]
