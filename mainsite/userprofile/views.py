from django.shortcuts import render, redirect
from django.contrib import auth
from django.core.context_processors import csrf
from userprofile.forms import UserProfileForm
from django.contrib.auth.decorators import login_required
from directory.models import Food, FoodMap, Company, FoodPhoto, CompanyPhoto
from userprofile.forms import MyRegistrationForm
import itertools
#from django.contrib.auth.forms import UserCreationForm

@login_required
def user_profile(request):
	if request.method == 'POST':
		form = UserProfileForm(request.POST, instance=request.user.profile)
		if form.is_valid():
			form.save()
			return redirect('userprofile.views.loggedin')

	else:
		iterator = itertools.count()
		user = request.user
		profile = user.profile
		form = UserProfileForm(instance=profile)
		foods = Food.objects.filter(user = user)
		foodMaps = FoodMap.objects.filter(user = user)
		companies = Company.objects.filter(user = user)
		companyPhotos = CompanyPhoto.objects.filter(user=user)
		foodPhotos = FoodPhoto.objects.filter(user=user)



	args = {}
	args.update(csrf(request))

	args['form'] = form
	args['user'] = user
	args['foods'] = foods
	args['foodMaps'] = foodMaps
	args['companies'] = companies
	args['companyPhotos'] = companyPhotos
	args['foodPhotos'] = foodPhotos
	args['iterator'] = iterator


	return render(request, 'userprofile/profile.html', args)



def login(request):
	c = {}
	c.update(csrf(request))
	return render(request, 'userprofile/login.html', c)

def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)

	if user is not None:
		auth.login(request, user)
		return redirect('userprofile.views.user_profile')
	else:
		return redirect('userprofile.views.user_profile')

def loggedin(request):
	return render(request, 'userprofile/loggedin.html', {'full_name': request.user.username})

def invalid_login(request):
	return render(request, 'userprofile/invalid_login.html')

def logout(request):
	auth.logout(request)
	return render(request, 'userprofile/logout.html')

def register_user(request):
	if request.method == 'POST':
		form = MyRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('userprofile.views.register_success')
	args = {}
	args.update(csrf(request))

	args['form'] = MyRegistrationForm()

	return render(request, 'userprofile/register.html', args)

def register_success(request):
	return render(request, 'userprofile/register_success.html')

# Create your views here.
