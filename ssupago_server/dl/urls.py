from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/predict', views.post_api, name='predict')
]