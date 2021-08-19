# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class CandidateInfo(models.Model):
    f_name = models.CharField(max_length=30)
    l_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    dob = models.DateField()
    exp = models.IntegerField()
    Grad = models.TextField(max_length=100)
    resume_att = models.FileField(upload_to='resume_docs/%Y/%m/%d/')
    domain = models.CharField(max_length=30)
    score_percent = models.CharField(max_length=30)
    college_name = models.CharField(max_length=100)
    grad_year = models.IntegerField()
    State = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
