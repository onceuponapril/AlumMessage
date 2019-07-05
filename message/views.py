from django.shortcuts import render, redirect
# from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.views.generic import CreateView,ListView

from .forms import MessageForm
from .models import Message
# Create your views here.

class HomePageView(generic.TemplateView):
    template_name = 'base.html'

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