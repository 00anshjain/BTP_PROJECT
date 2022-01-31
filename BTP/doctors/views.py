from django.shortcuts import render, redirect
# from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
from .models import *
from .forms import *
from django.utils.datastructures import MultiValueDictKeyError


def doctorRegister(request, pk):
    msg = None
    usr = Profile.objects.get(Did=pk)
    form = DoctorProfileForm(instance=usr)
    if request.method == 'POST':
        form = DoctorProfileForm(request.POST, request.FILES, instance=usr)
        if(form.is_valid()):
            # pk = request.POST.get('Did')
            form.save()
            msg = 'user created'
            # user = user.Did
            return redirect('doctorRegister2', pk)
        else:
            msg = 'form is not valid'
    # else:
    #     form = DoctorProfileForm()
    #     msg = 'Not found'
    return render(request, 'doctorRegister.html', {'form': form, 'msg': msg})


def doctorRegister2(request, pk):
    user = Profile.objects.get(Did=pk)
    # form = DoctorAvailablityForm(instance = user)

    form = DoctorAvailablityForm()
    if request.method == 'POST':
        # form = DoctorAvailablityForm(request.POST, instance = user)
        form = DoctorAvailablityForm(request.POST)
        # try:
        if(form.is_valid()):
            avail = form.save()
            user.available_time = avail
            user.save()
            # info = request.POST
            # user.available_time = info
            # user = user.save(commit = False)
            # user = user.Did
        # except MultiValueDictKeyError:
        #     info = False
        form.save()
        return redirect('doctorRegister3', pk)
    context = {'form': form}
    return render(request, 'doctorRegister2.html', context)


def doctorRegister3(request, pk):
    user = Profile.objects.get(Did=pk)
    # form = DoctorQualificationForm(instance = user)
    form = DoctorQualificationForm()
    if request.method == 'POST':
        form = DoctorQualificationForm(request.POST)
        if(form.is_valid()):

            info = form.save()
            user.qualifications = info
            user.save()
            # user.available_time
            form.save()

            return redirect('doctorLogin')
    context = {'form': form}
    return render(request, 'doctorRegister3.html', context)


def doctorProfile(request):
    return render(request, 'doctorProfile.html')


def doctorLogin(request):
    return render(request, 'doctorLogin.html')
