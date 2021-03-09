from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

def notLoggedUser(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('home:home'))
        else:
            return view_func(request,*args,**kwargs)
    return wrapper_func