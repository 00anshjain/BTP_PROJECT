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
    # pk is senderUsername
    reciever = request.user
    sender = User.objects.get(username = pk)

    # try:
    #     profileClient = ClientProfile.objects.get(username=username)
    #     profileDoctor = Profile.objects.get(Did = pk)
    #     isClient = True
    #     # msg = MessageData.objects.filter(clientProfile = profile)
        
    # except:
    #     profileDoctor = Profile.objects.get(username=username)
    #     profileClient = ClientProfile.objects.get(Cid = pk)
    #     isClient = False

    # if isClient:
    msg1 = MessageData.objects.filter(senderProfile = sender, recieverProfile = reciever).order_by('created')
    msg2 = MessageData.objects.filter(senderProfile = reciever, recieverProfile = sender).order_by('created')
    
    # msg1 = MessageData.objects.filter(senderProfile = sender, recieverProfile = reciever)
    # msg2 = MessageData.objects.filter(senderProfile = reciever, recieverProfile = sender)
    
    # print(type(msg1))
    msg = msg1 | msg2
    msg.order_by('created')
    # for item in msg2:
    #     msg1.append(item)
        # msg = MessageData.objects.filter(doctorProfile = profile)
    senderName = sender.first_name + ' ' + sender.last_name
    recieverName = reciever.first_name + ' ' + reciever.last_name
    context = {'messageRequests': msg, "senderProfile" : sender, "recieverProfile" : reciever, 'senderName' : senderName, 'recieverName' : recieverName}
    return render(request, 'conversations/viewConversation.html', context)


def inbox(request):
    username = request.user.username
    recieverProfile = User.objects.get(username = username)

    # try:
    #     senderProfile = ClientProfile.objects.get(username=username)
    #     isClient = True
    #     # msg = MessageData.objects.filter(clientProfile = profile)
        
    # except:
    #     senderProfile = Profile.objects.get(username=username)
    #     isClient = False
    #     # msg = MessageData.objects.filter(doctorProfile = profile)
    # if isClient:
    #     messageRequests = MessageData.objects.filter(clientProfile = profile)
    # else:

    # msgRequests = MessageData.objects.filter(recieverProfile = recieverProfile)
    # senderSet = set()
    # messageRequests = MessageData.objects.none()
    # for msg in msgRequests:
    #     if msg.senderProfile.username not in senderSet:
    #         messageRequests |= msg
    #         senderSet.add(msg.senderProfile.username)
        # messageRequests
    messageRequests  = MessageData.objects.filter(recieverProfile = recieverProfile)
    unreadCount = messageRequests.filter(isRead=False).count()
    context = {'messageRequests': messageRequests,
                'unreadCount': unreadCount,}
    return render(request, 'conversations/inbox.html', context)
    return redirect('account')  # for gadbad
    