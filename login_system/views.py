from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .forms import SignupForm
# from django.contrib import messages 


class UserRegisterView(generic.CreateView):
    form_class = SignupForm
    template_name =  'registration/register.html'
    success_url = reverse_lazy('login')
    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        
        return super().form_valid(form)