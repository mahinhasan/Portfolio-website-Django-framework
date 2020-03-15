# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

def home(request):
	my_dict = {'insert':"HELLO I AM FROM VIEWS"}
	return render(request,'blog/home.html',context=my_dict)

def about(request):
	ab = {'about_me':"I am cse Engineering!"}
	return render(request,'blog/about.html',context = ab)

# Create your views here.
