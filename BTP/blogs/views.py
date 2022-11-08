from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from .forms import BlogForm, ReviewForm
from .models import Blog
from doctors.models import Profile
from django.contrib import messages
# Create your views here.
from .utils import searchBlogs


def blogs(request):
    blogs, search_query = searchBlogs(request)
    context = {'blogs': blogs, 'search_query': search_query}
    # blogs = Blog.objects.all()
    # context = {"blogs": blogs}
    return render(request, "blogs/blogs.html", context)

@login_required(login_url="doctorLogin")
def blog(request, pk):
    blogObj = Blog.objects.get(id=pk)
    usr = request.user.username
    profile = Profile.objects.get(username=blogObj.owner.username)
    form  = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.blog = blogObj 
        review.owner = profile
        review.save()

        #Update blog count
        messages.success(request, 'Your review was successfully submitted!')

    return render(request, "blogs/single-blog.html", {"blog": blogObj, "form": form})


@login_required(login_url="doctorLogin")
def createBlog(request):
    usr = request.user.username
    profile = Profile.objects.get(username=usr)
    form = BlogForm()

    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.owner = profile
            blog.save()
            return redirect('blogs')

    context = {"form": form}
    return render(request, "blogs/blog_form.html", context)


@login_required(login_url="doctorLogin")
def updateBlog(request, pk):
    profile = request.user.profile
    blog = profile.project_set.get(id=pk)
    form = BlogForm(instance=blog)

    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect("blogs")

    context = {"form": form}
    return render(request, "blogs/blog_form.html", context)


@login_required(login_url="doctorLogin")
def deleteBlog(request, pk):
    profile = request.user.profile
    blog = profile.project_set.get(id=pk)
    if request.method == "POST":
        blog.delete()
        return redirect("blogs")
    context = {"object": blog}
    return render(request, "delete_template.html", context)
