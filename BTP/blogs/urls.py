from django.urls import path
from django.urls.resolvers import URLPattern
from . import views


urlpatterns = [
    path("", views.blogs, name="blogs"),
    path("blog/<str:pk>", views.blog, name="blog"),
    path("create-blog/", views.createBlog, name="create-blog"),
    path("update-blog/<str:pk>", views.updateBlog, name="update-blog"),
    path("delete-blog/<str:pk>", views.deleteBlog, name="delete-blog"),
]
