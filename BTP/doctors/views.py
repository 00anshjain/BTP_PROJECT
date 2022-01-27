from django.shortcuts import render, redirect
# from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
from .models import *
from .forms import *


def doctorRegister(request):
    msg = None
    if request.method == 'POST':
        form = DoctorProfileForm(request.POST)

        if(form.is_valid()):
            user = form.save()

            msg = 'user created'
        else:
            msg = 'form is not valid'
    else:
        form = DoctorProfileForm()
        msg = 'Not found'
    return render(request, 'doctorRegister.html', {'form': form, 'msg': msg})
