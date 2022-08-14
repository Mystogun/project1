from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.show, name="show"),
    path("search/", views.search, name="search"),
    path("new/", views.new, name="new"),
    path("store/", views.store, name="store"),
    path("edit/<str:title>", views.edit, name="edit"),
    path("save/", views.save_edit, name="save"),
    path("random", views.random_entry, name="random")
]
