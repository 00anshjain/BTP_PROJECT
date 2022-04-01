from django.shortcuts import render, redirect
# from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
from .models import *
from .forms import *
# from django.db.models import Q

from django.contrib import messages
from django.utils.datastructures import MultiValueDictKeyError
# from .utils import searchDoctors


def clientRegister(request, pk):
    msg = None
    usr = ClientProfile.objects.get(Cid=pk)
    form = ClientProfileForm(instance=usr)
    if request.method == 'POST':
        form = ClientProfileForm(request.POST, request.FILES, instance=usr)
        if(form.is_valid()):
            # pk = request.POST.get('Did')
            form.save()
            msg = 'user created'
            # user = user.Did
            return redirect('allDoctors')
            # return redirect('doctorRegister3', pk)
        else:
            msg = 'form is not valid'
        # else:
        #     form = DoctorProfileForm()
        #     msg = 'Not found'
    return render(request, 'clients/clientRegister.html', {'form': form, 'msg': msg})


def clientAccount(request):
    profile = request.user.profile
    # skills = profile.skill_set.all()
    # projects = profile.project_set.all()
    # context = {"profile": profile, "skills": skills, "projects": projects}
    context = {"profile": profile}
    return render(request, 'clients/clientAccount.html', context)
