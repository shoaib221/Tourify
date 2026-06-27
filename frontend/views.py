from django import views
from django.contrib import messages, auth
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User, auth
from django.forms import ValidationError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django import views
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.hashers import make_password, check_password





class Index(views.View):
    
    def get(self, request):
        return render(request, "index.html")
    


class Test(views.View):
    
    def get(self, request):
        return render(request, "test-1.html")
    
