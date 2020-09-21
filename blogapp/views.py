from django.shortcuts import render, redirect
from django.http import HttpResponse
from blogapp.models import Blog, BlogCategory, BlogSeries
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm


# Create your views here.

def homepage(request):
    categories = BlogCategory.objects.all()

    return render(request, 'categories.html', {'categories': categories})


def single_slug(request, single_slug):
    categories = [c.category_slug for c in BlogCategory.objects.all()]
    if single_slug in categories:
        matching_series = BlogSeries.objects.filter(blog_category__category_slug=single_slug)

        series_urls = {}
        for match in matching_series.all():
            part_one = Blog.objects.filter(blog_series__blog_series=match.blog_series).earliest("blog_published")
            series_urls[match] = part_one.blog_slug
        return render(request, 'category.html', {"part_ones": series_urls})

    blogs = [b.blog_slug for b in Blog.objects.all()]
    if single_slug in blogs:
        this_blog = Blog.objects.get(blog_slug=single_slug)
        blogs_from_series = Blog.objects.filter(blog_series__blog_series=this_blog.blog_series).order_by("blog_series")
        blog_index = list(blogs_from_series).index(this_blog)
        return render(request, 'blog.html', {'blog': this_blog, 'sidebar': blogs_from_series, 'blog_index': blog_index})

    return HttpResponse(f"{single_slug} does not ")


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New Account Created {username}")
            login(request, user)
            messages.info(request, f"You are now logged in as {username}")
            return redirect("blogapp:homepage")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}:{form.error_messages[msg]}")
    form = NewUserForm
    return render(request, 'register.html', {'form': form})


def logout_from_app(request):
    logout(request)
    messages.info(request, f"successfully logout!")
    return redirect("blogapp:homepage")


def login_app(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"successfully login")
                return redirect("blogapp:homepage")
            else:
                messages.error(request, f"Invalid username or password")
        else:
            messages.error(request, f"Invalid username or password")

    form = AuthenticationForm
    return render(request, 'login.html', {'form': form})
