from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.http import (HttpResponseRedirect,HttpResponse)
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import loginForm

#@login_required(login_url='/login/')
def view_index(request):
	return render_to_response('index.html',
			context_instance=RequestContext(request))


def view_login(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect("/")
			else:
				return HttpResponse("el usuario no esta activo")
		else:
			return HttpResponse("password o usuario incorrecto")
	else:
		form = loginForm()
		ctx = {'form':form}
		return render_to_response("home/login.html",ctx,
				context_instance=RequestContext(request))


def view_logout(request):
	logout(request)
	return HttpResponseRedirect("/login/")


def view_cats(request):
	return render_to_response("home/index.html",
				context_instance=RequestContext(request))