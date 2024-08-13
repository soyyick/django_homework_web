from django.urls import path
from . import views

urlpatterns = [
    path("", views.indexPage, name="index"),
    path("about/", views.aboutPage, name="about"),
    path("contact/", views.contactPage, name="contact"),
    path("table/", views.tablePage, name="table"),
    path("card/", views.cardPage, name="card"),
    path("color/", views.cardColorPage, name="color"),
]