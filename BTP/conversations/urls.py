from django.urls import path
from . import views

urlpatterns = [
    path("inbox/", views.inbox, name="inbox"),
    path("viewConversation/<str:pk>/", views.viewConversation, name="viewConversation"),
    path("appointmentForm/<str:pk>/", views.makeAppointment, name="makeAppointment"),
    path("appointmentRequest/<str:pk>/", views.appointmentRequest, name="appointmentRequest"),
    path("handleRequest/", views.handleRequest, name="handleRequest"),
    path("paymentConfirmation/", views.paymentConfirmation, name="paymentConfirmation"),
    path("paytm/", views.paytm, name="paytm"),
    
]
