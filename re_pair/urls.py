from django.urls import path
from . import views

app_name = "re_pair"

urlpatterns = [
    path("", views.index, name="index"),
    path("detail/<int:pk>/", views.detail, name="detail"),
    path("create/", views.create, name="create"),
    path("new/", views.new, name="new"),
    path("edit/<int:pk>/", views.edit, name="edit"),
    path("detail/<int:pk>/delete/<int:review_pk>/", views.delete, name='delete'),
    path("update/<int:pk>/", views.update, name="update"),
    path("inform/", views.inform, name="inform"),
    path("inform_new/", views.inform_new, name="inform_new"),
    path("inform_create/", views.inform_create, name="inform_create"),
    path("inform_edit/<int:pk>/", views.inform_edit, name="inform_edit"),
    path("inform_update/<int:pk>/", views.inform_update, name="inform_update"),
    path("inform_delete/<int:pk>/", views.inform_delete, name="inform_delete"),   
]
