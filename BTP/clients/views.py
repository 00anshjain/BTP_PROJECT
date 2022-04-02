from django.contrib.auth.decorators import login_required
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
        form = ClientProfileForm(request.POST, request.FILES,   instance=usr)
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


@login_required(login_url='doctorLogin')
def clientAccount(request):
    username = request.user.username
    print(username)
    try:
        profile = ClientProfile.objects.get(username=username)
    except:
        profile = None
    # if ClientProfile.objects.filter(username=username).count() != 0:
    if profile is not None:
        # pk = request.user.id
        # # print(pk)
        # try:
        #     profile = ClientProfile.objects.get(username=username)
        # except:
        #     print('Multi Value Dict Error')

        # print(profile)
        # print(profile.name)
        # profile = request.user.profile
        # skills = profile.skill_set.all()
        # projects = profile.project_set.all()
        # context = {"profile": profile, "skills": skills, "projects": projects}
        context = {"profile": profile}
        return render(request, 'clients/clientAccount.html', context)
        # return render(request, 'clients/clientAccount.html')
    return redirect('account')


def updateClientProfile(request, pk):
    profile = ClientProfile.objects.get(Cid=pk)
    form = ClientProfileForm(instance=profile)

    if request.method == 'POST':
        form = ClientProfileForm(request.POST, request.FILES, instance=profile)
        print(profile)
        form.save()
        return redirect('clientAccount')
    context = {'form': form, 'pk': pk}
    return render(request, 'clients/updateClientProfile.html', context)
