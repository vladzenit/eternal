from django.contrib import admin
from django.urls import path
from gabe.views import gabe_view

app_name="gabe"

urlpatterns = [
    path('',gabe_view,name="cool_name"),
]
