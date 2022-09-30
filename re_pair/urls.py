from django.urls import path
from . import views

app_name = "re_pair"

urlpatterns = [
    path("", views.index),
    path("detail/", views.detail, name="detail"),
    path("create/", views.create, name="create"),
    path("new/", views.new, name="new"),
]
