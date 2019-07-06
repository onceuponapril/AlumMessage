from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('send/', views.SendView.as_view(), name='send'),
    path('receive/', views.ReceiveView.as_view(), name='receive'),
    path('messagesList/', views.MessagesList.as_view(), name='messagesList')
]