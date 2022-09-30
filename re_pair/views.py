from django.shortcuts import render, redirect
from .models import Review

# Create your views here.
def index(request):
    review = Review.objects.all()
    context = {
        "review": review,
    }
    return render(request, "re_pair/index.html", context)


def detail(request):
    return render(request, "re_pair/detail.html")


def new(request):
    return render(request, "re_pair/new.html")


def create(request):
    title = request.GET.get("title")
    content = request.GET.get("content")
    Review.objects.create(title=title, content=content)

    context = {
        "title": title,
        "content": content,
    }

    return redirect("re_pair:index")
