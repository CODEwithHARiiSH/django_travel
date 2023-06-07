from . import views

from django.urls import path, include

urlpatterns = [


    path('', views.fun, name='fun'),

]
