

from doctors.views import Profile
from .models import *
from django.db.models import Q


def searchDoctors(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    profiles = Profile.objects.filter(
        Q(name__icontains=search_query) | Q(location__icontains=search_query) | Q(speciality__icontains=search_query))
    return profiles, search_query
