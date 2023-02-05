# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from datetime import datetime, time, timedelta
from django.utils import timezone

# Create your models here.

class Categories(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)
    name = models.CharField(db_column='name', max_length=255, blank=False, null=False)  # Field name made lowercase.
    datecreated = models.DateTimeField(blank=True, null=True, default=timezone.now)

    class Meta:
        managed = True
        db_table = 'categories'

class Authors(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)
    name = models.CharField(db_column='Name', max_length=105, blank=False, null=False)  # Field name made lowercase.
    surname  = models.CharField(db_column='Surname', max_length=105, blank=False, null=False)  # Field name made lowercase.
    job = models.TextField(db_column='job', blank=True, null=True)  # Field name made lowercase.
    datecreated = models.DateTimeField(blank=True, null=True, default=timezone.now)

    class Meta:
        managed = True
        db_table = 'authors'

class Articles(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=255)  # Field name made lowercase.
    summary = models.CharField(db_column='Summary', max_length=255)  # Field name made lowercase.
    content = models.TextField(db_column='Content')  # Field name made lowercase.
    author = models.ForeignKey(Authors, on_delete=models.DO_NOTHING, null=True)
    category = models.ForeignKey(Categories, on_delete=models.DO_NOTHING, null=True)
    published = models.IntegerField(db_column='Published', blank=True, null=True, default=0)  # Field name made lowercase.
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'articles'



