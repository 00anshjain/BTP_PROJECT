from http import client
from django.shortcuts import render, redirect
# from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *
from django.contrib import messages
from doctors.models import Profile
from clients.models import ClientProfile
import random
from django.core.mail import send_mail
from django.conf import settings


# from django.conf import settings
# User = settings.AUTH_USER_MODEL


# Create your views here.
def main(request):
    return redirect('allDoctors')


def index(request):
    return render(request, 'index.html')


def GenerateOTP(user):
    user_otp = random.randint(100000, 999999)
    UserOTP.objects.create(user=user, otp=user_otp)
    mess = f"hello {user.username}, \n Your OTP is {user_otp}\nThanks!"

    send_mail(
        "Welcome to DocIt - Verify your Email", 
        mess,
        settings.EMAIL_HOST_USER,
        [user.email],
        fail_silently=False
    )

def register(request):
    msg = None
    page = "register"
    if request.method == 'POST':
        get_otp = request.POST.get('otp')

        if get_otp:
            get_user = request.POST.get('user')
            user = User.objects.get(username=get_user)
            tcp = TempDoctorProfile.objects.get(username = user.username)
            
            # pk = tcp.TempCid

            # usr = Profile.objects.get(username=get_user)

            if int(get_otp) == UserOTP.objects.filter(user=user).last().otp:
                user.is_active = True
                user.save()

                messages.success(
                    request, f"User account was created for {user.email}")
                # login(request, get_user)
                # print(tcp.email)
                Profile.objects.create(username = tcp.username, name = tcp.name, email=tcp.email, age=tcp.age, gender=tcp.gender)
                pk = Profile.objects.get(username=tcp.username).Did
                tcp.delete()
                return redirect('doctorRegister', pk)
            else:
                messages.error(request, "Wrong OTP!")
                # tcp.delete()
                return render(request, "verifyOTP.html", {'user': user})
                # return render(request, "users/verifyOTP.html", {'user': user, 'pk': pk})




        form = CustomUserCreationForm(request.POST)
        username = request.POST['username']
        try:
            tempProfile = TempDoctorProfile.objects.get(username = username)
            userProfile = User.objects.get(username=username)
            tempProfile.delete()
            userProfile.delete()
        except:
            pass
        if form.is_valid():
            name = request.POST['first_name'] + ' ' + request.POST['last_name']
            email = request.POST['email']
            age = request.POST['age']
            gender = request.POST['gender']
            username = request.POST['username']
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            TempDoctorProfile.objects.create(name=name, email=email, age=age, gender=gender, username=username, user=user)
            # pk = TempClientProfile.objects.get(username=username).Cid
            # print(pk)
            # Profile.objects.create(name=name, email=email,
            #                        age=age, gender=gender, username=username, user=user)
            # pk = Profile.objects.get(username=username).Did
            # print(pk)
            msg = 'user created'
            GenerateOTP(user)
            return render(request, "verifyOTP.html", {'user': user})

            # return redirect('doctorRegister', pk)
        else:
            msg = 'form is not valid'
    else:
        form = CustomUserCreationForm()
    context = {'form': form, 'page': page}
    return render(request, 'doctors/doctorRegistrationPage.html', context)



def registerClient(request):
    msg = None
    page = "register"
    if request.method == 'POST':
        get_otp = request.POST.get('otp')

        if get_otp:
            get_user = request.POST.get('user')
            user = User.objects.get(username=get_user)
            tcp = TempClientProfile.objects.get(username = user.username)
            
            # pk = tcp.TempCid

            # usr = Profile.objects.get(username=get_user)

            if int(get_otp) == UserOTP.objects.filter(user=user).last().otp:
                user.is_active = True
                user.save()

                messages.success(
                    request, f"User account was created for {user.email}")
                # login(request, get_user)
                # print(tcp.email)
                ClientProfile.objects.create(username = tcp.username, name = tcp.name, email=tcp.email, dob=tcp.dob, gender=tcp.gender)
                pk = ClientProfile.objects.get(username=tcp.username).Cid
                tcp.delete()
                return redirect('clientRegister', pk)
            else:
                messages.error(request, "Wrong OTP!")
                # tcp.delete()
                return render(request, "verifyOTP.html", {'user': user})
                # return render(request, "users/verifyOTP.html", {'user': user, 'pk': pk})



        form = CustomClientUserCreationForm(request.POST)
        username = request.POST['username']
        try:
            tempProfile = TempClientProfile.objects.get(username = username)
            userProfile = User.objects.get(username=username)
            tempProfile.delete()
            userProfile.delete()
        except:
            pass
        if form.is_valid():

            name = request.POST['first_name'] + ' ' + request.POST['last_name']
            email = request.POST['email']
            dob = request.POST['dob']
            gender = request.POST['gender']
            username = request.POST['username']
            user = form.save(commit=False)
            user.is_active = False
            user.save()
           
            TempClientProfile.objects.create(name=name, email=email, dob=dob, gender=gender, username=username, user=user)
            # pk = TempClientProfile.objects.get(username=username).Cid
            # print(pk)
            msg = 'user created'

            GenerateOTP(user)
            # user_otp = random.randint(100000, 999999)
            # UserOTP.objects.create(user=user, otp=user_otp)
            # mess = f"hello {user.username}, \n Your OTP is {user_otp}\nThanks!"

            # send_mail(
            #     "Welcome to DocIt - Verify your Email", 
            #     mess,
            #     settings.EMAIL_HOST_USER,
            #     [email],
            #     fail_silently=False
            # )

            return render(request, "verifyOTP.html", {'user': user})

            # return redirect('clientRegister', pk)
        else:
            msg = 'form is not valid'
    else:
        form = CustomClientUserCreationForm()
    context = {'form': form, 'page': page}
    return render(request, 'clients/clientRegistrationPage.html', context)


def bookAppointment(request):
    return render(request, 'bookAppointment.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def doctors(request):
    return render(request, 'doctors.html')


def review(request):
    return render(request, 'review.html')


def services(request):
    return render(request, 'services.html')


def doctorLogin(request):
    page = "login"
    if request.user.is_authenticated:
        return redirect("allDoctors")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "user does not exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:

            if ClientProfile.objects.filter(username=username).count() != 0:
                login(request, user)
                return redirect("index")
            else:
                login(request, user)
                return redirect("allDoctors")

        else:
            messages.error(request, "Username OR Password is incorrect")
    return render(request, 'doctors/doctorLogin.html')


def logoutUser(request):
    logout(request)
    messages.info(request, "user was logged out!")
    return redirect("doctorLogin")
