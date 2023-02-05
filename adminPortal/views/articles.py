# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core import serializers
from django.shortcuts import render, get_object_or_404, redirect 
from django.http import HttpResponseRedirect, Http404, HttpResponse, JsonResponse
from django.template.context_processors import csrf
from django.core.paginator import Paginator
from django.contrib import messages
from adminPortal.models import Articles, Categories, Authors
from adminPortal.serializers import ArticleSerializer
import requests
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.utils.html import escape
from django.template.loader import render_to_string
# from weasyprint import HTML

def articleview(request):
    latest_post_list = Articles.objects.order_by('-published_date')
    context = {
        'latest_post_list': latest_post_list,
    }
    return render(request, 'adminPortal/pages/articleList.html', context)

def newArticle(request):
    if 'useremail' not in request.session:
        return HttpResponseRedirect('/login')

    cat_list = Categories.objects.all()
    author_list = Authors.objects.all()
    context = {
        'title': 'New Articles',
        'categories': cat_list,
        'authors': author_list,
    }
    return render(request, 'adminPortal/pages/newArticle.html', context)

def submitNewArticle(request):
    try:
        title = request.POST.get('title', '')
        content = request.POST.get('content', '')
        author_id = request.POST.get('author_id', '')
        category_id = request.POST.get('category_id', '')
        published = request.POST.get('published', '')
        
        request_data = {"title":title, "content":content, "summary": content[0:50], "author_id":author_id, "category_id":category_id, "published":1 }
        # requestdata = request_data.json();
        valid_ser = ArticleSerializer(data=request_data)
        # return HttpResponse(valid_ser.is_valid())
        if valid_ser.is_valid():
            Articles.objects.create(title=title, content=content, summary= content[0:50], author_id=author_id, category_id=category_id, published=1)
            messages.success(request, 'Article Created Successfully')
            return HttpResponseRedirect('/articles')
        else:
            messages.warning(request, valid_ser.errors)
            return HttpResponseRedirect('/newarticle')
    except Exception as exception:
        messages.warning(request, exception)
        return HttpResponseRedirect('/newarticle')

def articleEditView(request, id):
    articleDetails = Articles.objects.filter(id=id).first()
    cat_list = Categories.objects.all()
    author_list = Authors.objects.all()
    context = {
        'articleDetails': articleDetails,
        'categories': cat_list,
        'authors': author_list,
    }
    return render(request, 'adminPortal/pages/editArticle.html', context)


def updateArticle(request):
    try:
        id = request.POST.get('id', '')
        title = request.POST.get('title', '')
        content = request.POST.get('content', '')
        author_id = request.POST.get('author_id', '')
        category_id = request.POST.get('category_id', '')

        request_data = {"title":title, 
                        "content":content,
                        "summary": content[0:50],
                        "author_id":author_id, 
                        "category_id":category_id,
                        "published":1
                        }

        # requestdata = json.dumps(request_data);
        valid_ser = ArticleSerializer(data=request_data)
        # return HttpResponse(requestdata)
        if valid_ser.is_valid():
            Articles.objects.update_or_create(id=id,defaults=request_data)
            messages.success(request, 'Updated Article Successfully')
            return HttpResponseRedirect('/articles')
        else:
            messages.warning(request, valid_ser.errors)
            return HttpResponseRedirect('/articles')
    except Exception as exception:
        messages.warning(request, exception)
        return HttpResponseRedirect('/articles')



