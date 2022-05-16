import imp
from django.shortcuts import render, redirect
# from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login

from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.db.models import Q
from django.contrib.auth.models import User

from django.contrib import messages
from django.utils.datastructures import MultiValueDictKeyError
from .utils import searchDoctors

import json
import os
from django.conf import settings
# from django.contrib import settings, DATA_ROOT


def doctorRegister(request, pk):
    msg = None
    usr = Profile.objects.get(Did=pk)
    form = DoctorProfileForm(instance=usr)
    if request.method == 'POST':
        form = DoctorProfileForm(request.POST, request.FILES, instance=usr)
        if(form.is_valid()):
            # pk = request.POST.get('Did')
            form.save()
            usr = Profile.objects.get(Did=pk)
            print('Medical council is')
            print(request.POST['stateMedicalCouncil'])
            usr.registrationNumber = request.POST['registrationNumber']
            usr.stateMedicalCouncil = request.POST['stateMedicalCouncil']
            usr.yearOfRegistration = request.POST['yearOfRegistration']
               
            usr.save()

            msg = 'user created'
            # user = user.Did
            return redirect('doctorRegister3', pk)
        else:
            msg = 'form is not valid'
            print(msg)
    # else:
    #     form = DoctorProfileForm()
    #     msg = 'Not found'
    input_file = open(os.path.join(settings.DATA_ROOT, 'StateMedicalCouncil.json'))
    medicalCouncilList = json.load(input_file)
    for item in medicalCouncilList:
        print(item)
    yearList = [r for r in range(1984, datetime.date.today().year+1)]
    

    return render(request, 'doctors/doctorRegister.html', {'form': form, 'msg': msg, 'medicalCouncilList': medicalCouncilList, 'yearList': yearList})


# def doctorRegister2(request, pk):
#     user = Profile.objects.get(Did=pk)
#     # form = DoctorAvailablityForm(instance = user)

#     form = DoctorAvailablityForm()
#     if request.method == 'POST':
#         # form = DoctorAvailablityForm(request.POST, instance = user)
#         form = DoctorAvailablityForm(request.POST)
#         # try:
#         if(form.is_valid()):
#             monday_from = request.POST['monday_from']
#             monday_to = request.POST['monday_to']
#             tuesday_from = request.POST['tuesday_from']
#             tuesday_to = request.POST['tuesday_to']
#             wednesday_from = request.POST['wednesday_from']
#             wednesday_to = request.POST['wednesday_to']
#             thursday_from = request.POST['thursday_from']
#             thursday_to = request.POST['thursday_to']
#             friday_from = request.POST['friday_from']
#             friday_to = request.POST['friday_to']
#             saturday_from = request.POST['saturday_from']
#             saturday_to = request.POST['saturday_to']
#             sunday_from = request.POST['sunday_from']
#             sunday_to = request.POST['sunday_to']
#             Availability.objects.create(
#                 monday_from=monday_from, monday_to=monday_to,
#                 tuesday_from=tuesday_from, tuesday_to=tuesday_to,
#                 wednesday_from=wednesday_from, wednesday_to=wednesday_to,
#                 thursday_from=thursday_from, thursday_to=thursday_to,
#                 friday_from=friday_from, friday_to=friday_to,
#                 saturday_from=saturday_from, saturday_to=saturday_to,
#                 sunday_from=sunday_from, sunday_to=sunday_to,
#                 profile=user,
#             )
#             # avail = form.save()
#             # user.available_time = avail
#             # user.save()
#             # info = request.POST
#             # user.available_time = info
#             # user = user.save(commit = False)
#             # user = user.Did
#         # except MultiValueDictKeyError:
#         #     info = False
#         # form.save()
#         return redirect('doctorRegister3', pk)
#     context = {'form': form}
#     return render(request, 'doctors/doctorRegister2.html', context)


def doctorRegister3(request, pk):
    user = Profile.objects.get(Did=pk)
    # form = DoctorQualificationForm(instance = user)
    # input_file = open('degree.json')
    # input_file = open(os.path.join(settings.DATA_ROOT, 'degree.json'))
    # json_array = json.load(input_file)

    # input_file = open(os.path.join(settings.DATA_ROOT, 'collegeList.json'))
    # collegeList = json.load(input_file)

    # for item in json_array:
    # print(collegeList)
    # Qualification.object.create(profile = user)
    # form = DoctorQualificationForm()
    if request.method == 'POST':
        # form = DoctorQualificationForm(request.POST)
        # if(form.is_valid()):
        degree_name = request.POST['selectDegree']
        degree_date = request.POST['degree_date']
        university = request.POST['selectUniversity']

        Qualification.objects.create(
            degree_name=degree_name,
            degree_date=degree_date,
            university=university,
            profile=user,
        )

        # info = form.save()
        # user.qualifications = info
        # user.save()
        # user.available_time
        # form.save()
        return redirect('allDoctors')
    input_file = open(os.path.join(settings.DATA_ROOT, 'degree.json'))
    degreeList = json.load(input_file)
    input_file = open(os.path.join(settings.DATA_ROOT, 'collegeList.json'))
    collegeList = json.load(input_file)
    context = {'degreeList': degreeList, 'collegeList': collegeList}
    return render(request, 'doctors/doctorRegister3.html', context)


def doctorProfile(request, pk):
    profile = Profile.objects.get(Did=pk)
    blogs = profile.blog_set.all()
    qualification = Qualification.objects.get(profile=pk)
    return render(request, 'doctors/doctorProfile.html', {'profile': profile, 'blogs': blogs, 'qualification': qualification})


def updateDoctorProfile(request, pk):
    profile = Profile.objects.get(Did=pk)
    form = DoctorProfileForm(instance=profile)

    if request.method == 'POST':
        # councilName = request.POST.get('selectCouncil')
        # print(councilName)
        form = DoctorProfileForm(request.POST, request.FILES, instance=profile)


        # form.save()
        return redirect('allDoctors')
    input_file = open(os.path.join(settings.DATA_ROOT, 'StateMedicalCouncil.json'))
    medicalCouncilList = json.load(input_file)
    
    context = {'form': form, 'pk': pk, 'medicalCouncilList': medicalCouncilList}
    return render(request, 'doctors/updateDoctorProfile.html', context)


# def updateDoctorAvailablity(request, pk):
#     profile = Profile.objects.get(Did=pk)
#     availablity = Availability.objects.get(profile=profile)
#     form = DoctorAvailablityForm(instance=availablity)
#     if request.method == 'POST':
#         form = DoctorAvailablityForm(
#             request.POST, request.FILES, instance=availablity)
#         form.save()
#         return redirect('allDoctors')
#     context = {'form': form}
#     return render(request, 'doctors/updateDoctorAvailablity.html', context)


def allDoctors(request):
    profiles, search_query = searchDoctors(request)
    context = {'profiles': profiles, 'search_query': search_query}
    return render(request, 'doctors/allDoctors.html', context)


@login_required(login_url='doctorLogin')
def userAccount(request):
    # profile = request.user.profile
    # skills = profile.skill_set.all()
    # projects = profile.project_set.all()
    # context = {"profile": profile, "skills": skills, "projects": projects}
    username = request.user.username
    print(username)
    try:
        profile = Profile.objects.get(username=username)
        # print(profile)
    except:
        profile = None
    # print(profile)
    # if ClientProfile.objects.filter(username=username).count() != 0:
    if profile is not None:
        blogs = profile.blog_set.all()
        qualification = Qualification.objects.get(profile=profile)
        context = {"profile": profile, "blogs": blogs, "qualification": qualification}
        return render(request, 'doctors/account.html', context)
    return redirect('allDoctors')
