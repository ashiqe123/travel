from django.urls import path

from travelapp import views

urlpatterns = [

    path('',views.home,name='demo')
]
