"""TDM_V1 URL Configuration

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
from . import views
from django.conf.urls import url, include
from django.views.generic import TemplateView

from . import views


urlpatterns = [

    url(r'^Mulesoft',views.Mulereport , name='mulesoft'),
    url(r'^aggregate', views.SFDCreport, name='salesforce'),
    url(r'^event', views.Eventreport, name='event'),

]

    #url(r'^Reports/$', views.reports, name='reports'),
    #url(r'^Aggregate',views.sales, name='salesforce'),
    #url(r'^Salesforce',views.salesforce, name='salesforce'),
    #url(r'^Cloudhub', views.cloudhub, name='cloudhub'),
    #url(r'^salesforce1',views.salesforce1, name='salesforce'),
    # url(r'^aggregate',views.sales1, name='salesforce'),
    # url(r'^$', views.reports, name='index'),
    # url(r'^Mulesoft',views.mulesoft , name='mulesoft'),



