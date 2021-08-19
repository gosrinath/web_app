# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import CandidateInfo
from . import data_process

# Create your views here.
def refdetails(request):
    if request.method == 'POST' and 'addtodb' in request.POST:
        dbo = CandidateInfo()
        dbo.f_name = request.POST.get('firstName')
        dbo.l_name = request.POST.get('lastName')
        dbo.email = request.POST.get('email')
        dbo.dob = request.POST.get('dob')
        dbo.exp = request.POST.get('exp')
        dbo.Grad = request.POST.get('graduation')
        dbo.resume_att = request.POST.get('resumeupload')
        dbo.domain = request.POST.get('domain')
        dbo.score_percent = request.POST.get('percentage')
        dbo.college_name = request.POST.get('college')
        dbo.grad_year = request.POST.get('year')
        dbo.State = request.POST.get('state')
        dbo.country = request.POST.get('country')
        dbo.save()
    if request.method == 'POST' and 'showdb' in request.POST:
        return render(request, 'showdatabase.html', {"payl": data_process.get_from_db()})
    if request.method == 'POST' and 'cleardb' in request.POST:
        return render(request, 'showdatabase.html', {"payl": data_process.clear_from_db()})
    return render(request, 'refdetailspage.html')
