from django.urls import path
from . import views

urlpatterns = [
    path("inbox/", views.inbox, name="inbox"),
    path("viewConversation/<str:pk>/", views.viewConversation, name="viewConversation"),
    path("appointmentForm/<str:pk>/", views.makeAppointment, name="makeAppointment"),
    
]
