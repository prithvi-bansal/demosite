from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth.views import LoginView

# Create your views here.

class UserLogin(LoginView):
    template_name = 'registration/login.html'    
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('dashboard')


class UserSignup(FormView):
    template_name = 'registration/signup.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(UserSignup, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return reverse_lazy('dashboard')
        return super(UserSignup, self).get(*args, **kwargs)


