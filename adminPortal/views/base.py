# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core import serializers
from django.shortcuts import render, get_object_or_404, redirect 
from django.http import HttpResponseRedirect, Http404, HttpResponse, JsonResponse
from django.template.context_processors import csrf
from django.contrib.auth import authenticate, login, logout
from adminPortal.serializers import AdminLoginSerializer
from django.contrib import messages
import requests
import json
from django.template.loader import render_to_string
# from weasyprint import HTML


def ping(request):
    return HttpResponse("00")
    
def login(request):
    context = {
        'title': 'Login',
    }
    return render(request, 'adminPortal/login.html', context)

def authview(request):
    try:
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        request_data = {"email":email, "password":password}
        djson = json.dumps(request_data)
        valid_ser = AdminLoginSerializer(data=request_data)
        # return HttpResponse(ljson)
        if valid_ser.is_valid():
            request.session['useremail'] = request_data['email']
            return HttpResponseRedirect('/articles')
        else:
            messages.warning(request, 'Invalid details')
            return HttpResponseRedirect('/login')
    except Exception as exception:
        messages.warning(request, exception)
        return HttpResponseRedirect('/login')
        # return HttpResponse(exception)

def logoutview(request):
    del request.session['useremail']
    messages.warning(request, 'Successfully Looged Out')
    return HttpResponseRedirect('/login')


def index(request):
    if 'jwttoken' not in request.session:
        return HttpResponseRedirect('/login')

    context = {
        'title': 'Welcome',
        # 'guarantorlist': guarantorlist,
    }
    return render(request, 'adminPortal/index.html', context)