from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm


from .forms import MessageForm
from .models import Message
# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
        
class SendView(CreateView):
    model = Message
    template_name = 'send.html'
    form_class = MessageForm
    success_message = " Message Successfully Sent"

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request):
        form = MessageForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect(post) 
        return render(request, 'send.html', {'form': form})

    def get(self, request):
        form = MessageForm()
        return render(request, 'send.html', {'form': form})


class ReceiveView(ListView):
    model = Message
    template_name = 'receive.html'



class MessagesList(ListView):
    model = Message
    template_name = 'messagesList.html'

    def get_queryset(self):
        query = self.request.GET['q']
        message_list = Message.objects.filter(receiver=query)
        return message_list
