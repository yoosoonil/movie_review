from django.shortcuts import render, redirect
from .models import Review, Inform
from django.db.models import Avg
# Create your views here.
def index(request):
    review = Review.objects.all()
    inform = Inform.objects.all()
    rate_수리남 = Review.objects.filter(title__startswith="수리남").aggregate(Avg('star'))
    rate_스파이 = Review.objects.filter(title__startswith="스파이패밀리").aggregate(Avg('star'))
    rate_오징어 = Review.objects.filter(title__startswith="오징어게임").aggregate(Avg('star'))
    rate_우영우 = Review.objects.filter(title__startswith="이상한변호사:우영우").aggregate(Avg('star'))
    rate_종이 = Review.objects.filter(title__startswith="종이의집").aggregate(Avg('star'))
    rate_지옥 = Review.objects.filter(title__startswith="지옥").aggregate(Avg('star'))

    context = {
        "review": review,
        "inform" : inform,
        "rate_수리남" : rate_수리남,
        "rate_스파이" : rate_스파이,
        "rate_오징어" : rate_오징어,
        "rate_우영우" : rate_우영우,
        "rate_종이" : rate_종이,
        "rate_지옥" : rate_지옥,
    }
    return render(request, "re_pair/index.html", context)


def detail(request, pk):
    inform = Inform.objects.get(id=pk)
    review = Review.objects.all()
    context = {
        "inform": inform,
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


def edit(request, pk):
    # get 메소드를 사용해서 특정 pk 데이터를 불러온다.
    review = Review.objects.get(pk=pk)
    context = {
        "review": review,
    }
    return render(request, "re_pair/edit.html", context)

def delete(request, pk, review_pk):
    review = Review.objects.get(pk=review_pk)
    review.delete()
    return redirect('re_pair:detail', pk)

def update(request, pk):
    review = Review.objects.get(pk=pk)
    title_ = request.GET.get("title")
    content_ = request.GET.get("content")

    review.title = title_
    review.content = content_

    review.save()
    
    return redirect("re_pair:index")





def inform(request):
    inform = Inform.objects.all()
    
    context = {
        "inform" : inform
    }
    
    return render(request, "re_pair/inform.html", context)


def inform_new(request):
    return render(request, "re_pair/inform_new.html")

def inform_create(request):
    title = request.POST.get("title")
    content = request.POST.get("content")
    Inform.objects.create(title=title, content=content)

    context = {
        "title": title,
        "content": content,
    }

    return redirect("re_pair:inform")

def inform_delete(pk):
    Inform.objects.get(id=pk).delete()
    return redirect("re_pair:inform")


def inform_edit(request, pk):
    # get 메소드를 사용해서 특정 pk 데이터를 불러온다.
    inform = Inform.objects.get(pk=pk)
    context = {
        "inform": inform,
    }
    return render(request, "re_pair/inform_edit.html", context)

def inform_update(request, pk):
    inform = Inform.objects.get(pk=pk)

    title_ = request.GET.get("title")
    content_ = request.GET.get("content")
    opendate_ = request.GET.get("opendate")
    
    inform.title = title_
    inform.content = content_
    inform.opendate = opendate_
    
    inform.save()

    return redirect("re_pair:inform")

