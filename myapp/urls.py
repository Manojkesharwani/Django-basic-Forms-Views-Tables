from django.urls import path
from . import views
from .views import forms

urlpatterns = [
    path('',views.index,name='home'),
    path('mydata/',forms.as_view(),name='post'),
]
