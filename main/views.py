from django.shortcuts import render
from django.conf import settings
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.clickjacking import xframe_options_deny
from django.conf import settings


#from rest_framework.parsers import JSONParser



basepath=settings.BASE_DIR


@xframe_options_deny
@login_required(login_url='/ADVAR/login')
def home(request):

    return render(request, basepath+'/main/templates/index.html')


def login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    print(user)
    if user is not None and user.is_active:
        auth.login(request, user)
        request.session.cycle_key()
        return HttpResponseRedirect('/ADVAR/')
    else:
        return HttpResponseRedirect("login")


def logout_view(request):
    auth.logout(request)
    return HttpResponseRedirect('/ADVAR/login')

