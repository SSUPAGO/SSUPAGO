from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_api, name='index'),
    path('/predict', views.post_api, name='predict')
]