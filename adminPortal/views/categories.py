# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core import serializers
from django.shortcuts import render, get_object_or_404, redirect 
from django.http import HttpResponseRedirect, Http404, HttpResponse, JsonResponse
from django.template.context_processors import csrf
from django.contrib import messages
from adminPortal.models import Categories
from adminPortal.serializers import CategorySerializer
import requests
import json
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.utils.html import escape
from django.template.loader import render_to_string
# from weasyprint import HTML


def categoriesview(request):
    cat_list = Categories.objects.all()
    context = {
        'cat_list': cat_list,
    }
    return render(request, 'adminPortal/pages/categoryList.html', context)

def newCategory(request):
    if 'useremail' not in request.session:
        return HttpResponseRedirect('/login')

    context = {
        'title': 'New Category',
    }
    return render(request, 'adminPortal/pages/newCategory.html', context)

def submitNewCategory(request):
    try:
        name = request.POST.get('name', '')
        request_data = {"name":name}
        # requestdata = request_data.json();
        valid_ser = CategorySerializer(data=request_data)
        # return HttpResponse(valid_ser.is_valid())
        if valid_ser.is_valid():
            Categories.objects.create(name=name)
            messages.success(request, 'Category Created Successfully')
            return HttpResponseRedirect('/categories')
        else:
            messages.warning(request, valid_ser.errors)
            return HttpResponseRedirect('/newcategory')
    except Exception as exception:
        messages.warning(request, exception)
        return HttpResponseRedirect('/newcategory')

def categoryEditView(request, id):
    categoryDetails = Categories.objects.filter(id=id).first()
    context = {
        'categoryDetails': categoryDetails,
    }
    return render(request, 'adminPortal/pages/editCategory.html', context)


def updateCategory(request):
    try:
        id = request.POST.get('id', '')
        name = request.POST.get('name', '')

        request_data = {"name":name}

        # requestdata = json.dumps(request_data);
        valid_ser = CategorySerializer(data=request_data)
        # return HttpResponse(requestdata)
        if valid_ser.is_valid():
            Categories.objects.update_or_create(id=id,defaults=request_data)
            messages.success(request, 'Updated Category Successfully')
            return HttpResponseRedirect('/categories')
        else:
            messages.warning(request, valid_ser.errors)
            return HttpResponseRedirect('/categories')
    except Exception as exception:
        messages.warning(request, exception)
        return HttpResponseRedirect('/categories')