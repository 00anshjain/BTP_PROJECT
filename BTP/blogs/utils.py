

from blogs.views import *
from .models import *
from django.db.models import Q


def searchBlogs(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    blogs = Blog.objects.filter(
        Q(title__icontains=search_query))
        #  | Q(tags__icontains=search_query) )
        #  | Q(owner__icontains=search_query))
    return blogs, search_query
