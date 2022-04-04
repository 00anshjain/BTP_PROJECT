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


def createMessage(request):
    username = request.user.username
    try:
        profile = ClientProfile.objects.get(username=username)
        isClient = True
    except:
        profile = None
        isClient = False
    # form = MessageForm()
    # if profile is None :
    #     try:
    #         profile = ClientProfile.objects.get(username=username)
    #     except:
    #         profile = None
    # if request.method == 'POST':
        
def viewConversation(request, pk):
    username = request.user.username
    try:
        profileClient = ClientProfile.objects.get(username=username)
        profileDoctor = Profile.objects.get(Did = pk)
        isClient = True
        # msg = MessageData.objects.filter(clientProfile = profile)
        
    except:
        profileDoctor = Profile.objects.get(username=username)
        profileClient = ClientProfile.objects.get(Cid = pk)
        isClient = False

    # if isClient:
    msg = MessageData.objects.filter(doctorProfile = profileDoctor, clientProfile = profileClient)

        # msg = MessageData.objects.filter(doctorProfile = profile)
    context = {'messageRequests': msg, "ClientUser" : profileClient.username, "DoctorUser" : profileDoctor.username, "isClient" : isClient}
    return render(request, 'conversations/viewConversation.html', context)


def inbox(request):
    username = request.user.username
    try:
        profile = ClientProfile.objects.get(username=username)
        isClient = True
        # msg = MessageData.objects.filter(clientProfile = profile)
        
    except:
        profile = Profile.objects.get(username=username)
        isClient = False
        # msg = MessageData.objects.filter(doctorProfile = profile)
    if isClient:
        messageRequests = MessageData.objects.filter(clientProfile = profile)
    else:
        messageRequests = MessageData.objects.filter(doctorProfile = profile)
    unreadCount = messageRequests.filter(isRead=False).count()
    context = {'messageRequests': messageRequests,
                'unreadCount': unreadCount, 
                'isClient': isClient}
    return render(request, 'conversations/inbox.html', context)
    return redirect('account')  # for gadbad
    
