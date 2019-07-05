from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('send/', views.SendView.as_view(), name='send'),

]