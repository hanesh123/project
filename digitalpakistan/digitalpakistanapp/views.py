from django.forms.widgets import DateTimeBaseInput
from django.template.defaultfilters import capfirst, title
from django.views.generic.base import TemplateView
from rest_framework.fields import empty
from django.shortcuts import redirect, render
from django.http import HttpResponse,HttpResponseRedirect
from django.views import View
from .models import *
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from django.shortcuts import (get_object_or_404,
                              render, 
                              HttpResponseRedirect)
from django.contrib.auth  import authenticate, get_user,  login, logout
from django.contrib import messages

from django.contrib.auth.models import User




# ********************** Authentications Functions *******************************

class loginPage(View):
    # form_class = MyForm
    initial = {'key': 'value'}
    template_name = 'dashboard/login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name,{"title":"Login"})

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        # print(user)
        # form = self.form_class(request.POST)
        if user is not None:
            login(request, user)
            # print(get_user(request)) 
            return redirect('dashboard')
        else:
            messages.info(request, 'Username OR password is incorrect')
            return HttpResponseRedirect('/failed/')



def logoutUser(request):
	logout(request)

	return redirect('login')


class changePassword(View):
    # form_class = MyForm
    initial = {'key': 'value'}
    template_name = 'dashboard/change_password.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name,{"title":"Change Password"})

    def post(self, request, *args, **kwargs):
        # username = request.POST.get('username')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        print(get_user(request))  


        if password2==password1:
            user = authenticate(request, username=get_user(request), password=password)
            # print(user)
            # form = self.form_class(request.POST)
            if user is not None:
                u = User.objects.get(username=get_user(request))
                u.set_password(password1)
                u.save()
                # login(request, user)
                # print(get_user(request)) 
                return redirect('login')
            else:
                messages.info(request, 'Password is incorrect')
                return HttpResponse('/failed due to pass incorrect/')
                # return HttpResponseRedirect('/failed/')
        else:
            messages.info(request, 'Password not matched')
            return HttpResponse('/failed due to pass not match/')
            # return HttpResponseRedirect('/failed/')


# *************************************************************************



# ********************** Dashboard Functions *******************************

def Dashboard(request):
    template_name = "dashboard/index.html"
    if get_user(request).is_authenticated:
        if request.method == "GET":
            return render(request, template_name)
            # return render(request, template_name,{"data":context})
    else:
        return render(request,'dashboard/login.html')

# ********************************************************************

# ********************** Website Functions *******************************


def Home(request):
    template_name = "website/index.html"
    if request.method == "GET":
        return render(request, template_name)



def contact(request):
    template_name = "website/contact.html"
    if request.method == "GET":
        return render(request, template_name)

def blog1(request):
    template_name = "website/blog.html"
    if request.method == "GET":
        return render(request, template_name)        
        
def blogdetails(request):
    template_name = "website/details.html"
    if request.method == "GET":
        return render(request, template_name)        
                

# ********************************************************************



