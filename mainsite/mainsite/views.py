from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf


def home(request):
	return render(request, 'mainsite/home.html')
