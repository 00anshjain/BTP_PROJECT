from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
# from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
from .models import *
from .forms import *

from django.core.mail import send_mail
from django.conf import settings
# from django.db.models import Q


# import jwt
import requests
import json
from time import time

import requests
import json
from datetime import datetime, timedelta
# import pytz

headers = {
    'Authorization': 'occvlk7x6r7o0ndol75wlbae8odkdn38yfbu15wkm4z7imowp3'
}




from django.contrib import messages
from django.utils.datastructures import MultiValueDictKeyError
# from .utils import searchDoctors



# Enter your API key and your API secret
API_KEY = 'QyIB14uZQ4WYX7b7MZS4rA'
API_SEC = 'b5M7SO7Fz3NTWEkqZWTzyPxpURNqOAo6CYFI'




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
    sender = User.objects.get(username=pk)
    isClient = False

    try:
        senderForImage = ClientProfile.objects.get(username=pk)
        # profileDoctor = Profile.objects.get(Did = pk)
        # isClient = True
        # msg = MessageData.objects.filter(clientProfile = profile)

    except:
        senderForImage = Profile.objects.get(username=pk)
        isClient = True
        # profileClient = ClientProfile.objects.get(Cid = pk)
        # isClient = False

    # if isClient:

    if request.method == 'POST':
        try:
            textData = request.POST['textInput']
        except:
            textData = None
        try:
            # imageFile = request.FILES['uploadImage'].read()
            imageFile = request.FILES['uploadImage']
        except:
            imageFile = None
        # print('HI')
        # print(textData)
        MessageData.objects.create(
            senderProfile=reciever, recieverProfile=sender, messageBody=textData, messageImage=imageFile)
        # return redirect({% url 'viewConversation' pk %})
        return redirect('viewConversation', pk)

    msg1 = MessageData.objects.filter(
        senderProfile=sender, recieverProfile=reciever).order_by('created')
    msg2 = MessageData.objects.filter(
        senderProfile=reciever, recieverProfile=sender).order_by('created')
    for item in msg1:
        item.isRead = True
        item.save()
    # msg1 = MessageData.objects.filter(senderProfile = sender, recieverProfile = reciever)
    # msg2 = MessageData.objects.filter(senderProfile = reciever, recieverProfile = sender)

    # print(type(msg1))
    msg = msg1 | msg2
    msg.order_by('created')
    # for item in msg:
    #     print(item.messageImage)
    # for item in msg2:
    #     msg1.append(item)
    # msg = MessageData.objects.filter(doctorProfile = profile)
    senderName = sender.first_name + ' ' + sender.last_name
    recieverName = reciever.first_name + ' ' + reciever.last_name

    # for item in msg1:
    #     print(item.senderProfile)
    # print('HIIIIIIIIIIIII')
    # for item in msg2:
    #     print(item.senderProfile)

    context = {'messageRequests': msg, "senderProfile": sender, "recieverProfile": reciever,
               'senderName': senderName, 'recieverName': recieverName, 'senderForImage': senderForImage, 'isClient': isClient}
    return render(request, 'conversations/viewConversation.html', context)


def inbox(request):
    username = request.user.username
    recieverProfile = User.objects.get(username=username)

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

    messageRequests = MessageData.objects.filter(
        recieverProfile=recieverProfile)
    # messageRequests2 = MessageData.objects.filter(senderProfile = recieverProfile)
    # for profile in messageRequests:
    #     if
    unreadCount = messageRequests.filter(isRead=False).count()
    context = {'messageRequests': messageRequests,
               'unreadCount': unreadCount, }
    return render(request, 'conversations/inbox.html', context)
    return redirect('account')  # for gadbad



def convert_date(datestring, time): #2022-04-28 23:30:00
    datelist = datestring.split(" ")
    if time=="start":
        returnstring = f'{datelist[0]}T{datelist[1]}+05:30'
    else:
        returnstring = f'{datelist[0]}T{datelist[1]}+04:30'
    datetimeobject = datetime.strptime(datestring, "%Y-%m-%d %H:%M:%S")
    # print(datetimeobject)
    
    return returnstring
# convert_date("2022-04-28 23:30:00")


def makeAppointment(request, pk):
    # pk is client username
    doctor = request.user
    client = User.objects.get(username = pk)
    form = AppointmentForm()

    if request.method == "POST":
        form = AppointmentForm(request.POST, instance = doctor)
        scheduleDate = request.POST['date']
        scheduleTime = request.POST['time']
        date_time_str = scheduleDate + " " + scheduleTime + ":00"
        # print(date_time_str)
        # date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')

        # start_time = convert_date(date_time_str, "start")
        # end_time = convert_date(date_time_str, "end")

        # date_time_utc = date_time_obj
        # print(type(date_time_utc))
        # 2022-04-28T05:00:11Z

        # time_utc_string = date_time_utc.strftime("%H:%M:%S")
        # # print(time_utc_string)
        # date_utc_string = date_time_utc.strftime("%Y-%m-%d")
        # # print(date_utc_string)
        # end_time_utc = date_time_obj - timedelta(hours=4, minutes=30)
        # end_time_utc_string = end_time_utc.strftime("%H:%M:%S")
        # # print(end_time_utc_string)
        # end_date_utc_string = date_time_utc.strftime("%Y-%m-%d")
        # # print(end_date_utc_string)

        # final_start_time = date_utc_string + "T" + time_utc_string + "Z"
        # final_end_time = end_date_utc_string + "T" + end_time_utc_string + "Z"


        # print(date_time_utc)
        # print("k")
        # print(date_time_obj)
        # print(type(date_time_obj))
        # print(type(scheduleTime))
        # print(scheduleTime)
        # print(scheduleDate)

        
        # def generateToken():
        #     token = jwt.encode(

        #         # Create a payload of the token containing
        #         # API Key & expiration time
        #         {'iss': API_KEY, 'exp': time() + 5000},

        #         # Secret used to generate token signature
        #         API_SEC,

        #         # Specify the hashing alg
        #         algorithm='HS256'
        #     )
        #     return token


        # # create json data for post requests
        # meetingdetails = {"topic": "The title of your zoom meeting",
        #                 "type": 2,
        #                 "start_time": f"{scheduleDate}T10: {scheduleTime}",
        #                 "duration": "45",
        #                 "timezone": "Asia/Kolkata",
        #                 "agenda": "test",

        #                 "recurrence": {"type": 1,
        #                                 "repeat_interval": 1
        #                                 },
        #                 "settings": {"host_video": "true",
        #                             "participant_video": "true",
        #                             "join_before_host": "False",
        #                             "mute_upon_entry": "False",
        #                             "watermark": "true",
        #                             "audio": "voip",
        #                             "auto_recording": "cloud"
        #                             }
        #                 }

        # # send a request with headers including
        # # a token and meeting details


        # def createMeeting():
        #     headers = {'authorization': 'Bearer ' + generateToken(),
        #             'content-type': 'application/json'}
        #     r = requests.post(
        #         f'https://api.zoom.us/v2/users/me/meetings',
        #         headers=headers, data=json.dumps(meetingdetails))

        #     print("\n creating zoom meeting ... \n")
        #     # print(r.text)
        #     # converting the output into json and extracting the details
        #     y = json.loads(r.text)
        #     join_URL = y["join_url"]
        #     meetingPassword = y["password"]

        #     # print(
        #     #     f'\n here is your zoom meeting link {join_URL} and your \
        #     #     password: "{meetingPassword}"\n')

        #     subject = 'Appointment with DocItMed'
        #     message = f"here's your appointment joining link and password.\nJoining Link: {join_URL}\nPassword: {meetingPassword}\nDate: {scheduleDate}\nTime: {scheduleTime}\n\nPlease join on time.\nThank You."
            
        #     send_mail(
        #         subject,
        #         message,
        #         settings.EMAIL_HOST_USER,
        #         [doctor.email, client.email],
        #         fail_silently=False,
        #     )

        
        def create_meeting(senderName, clientName, startDate, endDate, senderEmail, clientEmail, message, allDay=False):  # 2020-04-22 10:00:00
            json_data = {
                'title': f'DocItMed : Meeting Scheduled {senderName} - {clientName}',
                'created_by': {
                    'email': 'docitmed@gmail.com',
                },
                'dates': [
                    {
                        'all_day': allDay,
                        'date': convert_date(startDate, "start"),
                        'end_date': convert_date(endDate, "end"),
                        
                    },
                ],
                'places': [{"name": "Google Meet", "source": "Google Meet"}],
                'invitees': [{"email": senderEmail}, {"email": clientEmail}, {"email": "docitmed@gmail.com"}],
                'timezone': "Asia/Kolkata",
                'messages': {
                    'body': message
                },
                'confirmed': {
                    'flag': True
                }
            }
            response = requests.post(
                'https://api.vyte.in/v2/events', headers=headers, json=json_data)
            jsonResponse = json.loads(response.text)
            # print(jsonResponse)
            print(
                f"Meeting ID: {jsonResponse['_id']} \nPlace ID: {jsonResponse['places'][0]['_id']} \nDate ID: {jsonResponse['dates'][0]['_id']}")
            print(f"Meeting Link: {jsonResponse['places'][0]['address']}")

        # run the create meeting function
        # createMeeting()
        create_meeting('Dr. ' +doctor.first_name + ' ' + doctor.last_name, client.first_name + ' ' + client.last_name, date_time_str, date_time_str, doctor.email, client.email, "Hello! Please be on time.")


        
        return redirect('allDoctors')

    context = {'form': form}
    return render(request, 'conversations/appointmentForm.html', context)