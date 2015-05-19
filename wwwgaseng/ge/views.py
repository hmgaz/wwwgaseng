from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import login, logout

class LoginFormView(FormView):
    form_class = AuthenticationForm
    temlate_name = "ge/login.html"
    success_url = "/ge/"
    
    def form_valid(self, form):
        self.user = form.get_user()
        
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)
     
class LogoutView(View):
    def get(self, request):
        logout(request)
        
        return HttpResponseRedirect("/ge/")
# Create your views here.
