from django.shortcuts import render, redirect
from .models import Review
from django.db.models import Avg
# Create your views here.
def index(request):
    review = Review.objects.all()
    rate_수리남 = Review.objects.filter(title__startswith="수리남").aggregate(Avg('star'))
    rate_스파이 = Review.objects.filter(title__startswith="스파이패밀리").aggregate(Avg('star'))

    context = {
        "review": review,
        "rate_수리남" : rate_수리남,
        "rate_스파이" : rate_스파이,
    }
    return render(request, "re_pair/index.html", context)


def detail(request, pk):
    review = Review.objects.get(id = pk)
    context = {
        "review": review,
    }
    return render(request, "re_pair/detail.html", context)


def new(request):
    return render(request, "re_pair/new.html")


def create(request):
    title = request.GET.get("title")
    content = request.GET.get("content")
    star = request.GET.get("star")
    Review.objects.create(title=title, content=content, star=star)

    context = {
        "title": title,
        "content": content,
        "star": star,
    }

    return redirect("re_pair:index")


def edit(request, pk_):
    # get 메소드를 사용해서 특정 pk 데이터를 불러온다.
    review = Review.objects.get(pk=pk_)
    context = {
        "review": review,
    }
    return render(request, "re_pair/edit.html", context)


def update(request, pk_):
    review = Review.objects.get(pk=pk_)

    title_ = request.GET.get("title")
    content_ = request.GET.get("content")

    review.title = title_
    review.content = content_

    review.save()

    return redirect("re_pair:detail", review.pk)


def delete(request, pk):
    Review.objects.get(id=pk).delete()
    return redirect("re_pair:index")

def inform(request):
    return render(request, "re_pair/inform.html")