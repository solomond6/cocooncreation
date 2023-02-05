# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core import serializers
from django.shortcuts import render, get_object_or_404, redirect 
from django.http import HttpResponseRedirect, Http404, HttpResponse, JsonResponse
from django.template.context_processors import csrf
from django.contrib import messages
from adminPortal.models import Authors
from adminPortal.serializers import AuthorSerializer
import requests
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.utils.html import escape
from django.template.loader import render_to_string
# from weasyprint import HTML


def authorsview(request):
    author_list = Authors.objects.all()
    context = {
        'author_list': author_list,
    }
    return render(request, 'adminPortal/pages/authorList.html', context)

def newAuthor(request):
    if 'useremail' not in request.session:
        return HttpResponseRedirect('/login')

    context = {
        'title': 'New Author',
    }
    return render(request, 'adminPortal/pages/newAuthor.html', context)

def submitNewAuthor(request):
    try:
        name = request.POST.get('name', '')
        surname = request.POST.get('surname', '')
        job = request.POST.get('job', '')
        
        request_data = {"name":name, "surname":surname, "job":job }
        # requestdata = request_data.json();
        valid_ser = AuthorSerializer(data=request_data)
        # return HttpResponse(valid_ser.is_valid())
        if valid_ser.is_valid():
            Authors.objects.create(name=name, surname=surname, job=job)
            messages.success(request, 'Author Created Successfully')
            return HttpResponseRedirect('/authors')
        else:
            messages.warning(request, valid_ser.errors)
            return HttpResponseRedirect('/newauthor')
    except Exception as exception:
        messages.warning(request, exception)
        return HttpResponseRedirect('/newauthor')

def authorEditView(request, id):
    authorDetails = Authors.objects.filter(id=id).first()
    context = {
        'authorDetails': authorDetails,
    }
    return render(request, 'adminPortal/pages/editAuthor.html', context)


def updateAuthor(request):
    try:
        id = request.POST.get('id', '')
        name = request.POST.get('name', '')
        surname = request.POST.get('surname', '')
        job = request.POST.get('job', '')

        request_data = {"name":name, 
                        "surname":surname,
                        "job": job,
                        }

        # requestdata = json.dumps(request_data);
        valid_ser = AuthorSerializer(data=request_data)
        # return HttpResponse(requestdata)
        if valid_ser.is_valid():
            Authors.objects.update_or_create(id=id,defaults=request_data)
            messages.success(request, 'Updated Article Successfully')
            return HttpResponseRedirect('/authors')
        else:
            messages.warning(request, valid_ser.errors)
            return HttpResponseRedirect('/authors')
    except Exception as exception:
        messages.warning(request, exception)
        return HttpResponseRedirect('/authors')


