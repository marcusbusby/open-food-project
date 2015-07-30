from django.shortcuts import render, get_object_or_404
from .models import Food, Company, FoodMap, CompanyPhoto, FoodPhoto
from django.contrib.auth.decorators import login_required
from .forms import FoodForm, CompanyForm, ComponentForm, CompanyPhotoForm, FoodPhotoForm
from django.shortcuts import redirect

# import pdb; pdb.set_trace()

def search(request):
	if request.method == "GET":
		search_text = request.GET['search_text']
	else: 
		search_text = ''

	foods = Food.objects.filter(name__contains=search_text)
	companies = Company.objects.filter(name__contains=search_text)


	return render(request, 'directory/search.html', {'foods':foods, 'companies':companies})

def food_sort(request):
	if request.method == "GET":
		sort_value = request.GET['sort_value']

	foods = Food.objects.order_by(sort_value)

	return render(request, 'directory/food_sort.html', {'foods':foods})

def food_list(request):
	foods = Food.objects.all()
	fooddict = {}
	for food in foods:
		if food.slug in fooddict:
			fooddict[food.slug].append(food.company)
		else:
			fooddict[food.slug] = [food.name, food.company]
	#foods = Food.objects.all()
	return render(request, 'directory/food_list.html', {'foods': foods, 'fooddict': fooddict})

def food_detail(request, string):
	foods = Food.objects.filter(slug = string)
	photos = []
	foodmaps = []
	companies = []
	for food in foods:
		companies.append(food.company)
		photos.extend(FoodPhoto.objects.filter(food=food))
		foodmaps.extend(FoodMap.objects.filter(target=food))
	componentdict = {}

	for foodmap in foodmaps:
		if foodmap.component.name in componentdict:
			componentdict[foodmap.component.name][1].append(foodmap.amount)
		else:
			componentdict[foodmap.component.name] = [foodmap.component.slug,[foodmap.amount]]

	return render(request, 'directory/food_detail.html', {'foods': foods, 'photos':photos, 'companies': companies, 'componentdict': componentdict})

def food_entry(request, pk):
	food = get_object_or_404(Food, pk=pk)
	"""contents = food.get_view_contents
	photos = FoodPhoto.objects.filter(food=food)
	foodmaps = FoodMap.objects.filter(target=food)"""

	return render(request, 'directory/food_entry.html', {'food': food})

@login_required
def food_new(request):
	if request.method == "POST":
		form = FoodForm(request.POST)
		if form.is_valid():
			form.save(request.user)
			return redirect('directory.views.food_detail', pk=form.instance.pk)
	else:
		form = FoodForm()
	return render(request, 'directory/edit.html', {'form': form})

@login_required
def food_edit(request, pk):
	food = get_object_or_404(Food, pk=pk)
	if request.method == "POST":
		form = FoodForm(request.POST) #instance=food
		if form.is_valid():
			form.save(request.user, food)
			return redirect('directory.views.food_detail', pk=form.instance.pk)
	else:
		form = FoodForm(instance=food)
	return render(request, 'directory/edit.html', {'form': form})

@login_required
def food_delete(request,pk):
	food = get_object_or_404(Food, pk=pk)
	if request.user == food.user:
		food.delete()
		return redirect('userprofile.views.user_profile')

@login_required
def component_new(request):
	if request.method == "POST":
		form = ComponentForm(request.POST)
		if form.is_valid():
			form.save(request.user)
			return redirect('directory.views.food_list')
	else:
		form = ComponentForm()
	return render(request, 'directory/edit.html', {'form': form})

@login_required
def component_delete(request,pk):
	foodmap = get_object_or_404(FoodMap, pk=pk)
	if request.user == foodmap.user:
		foodmap.delete()
		return redirect('userprofile.views.user_profile')

def company_list(request):
	companies = Company.objects.all()
	companydict = {}
	for company in companies:
		if company.slug in companydict:
			companydict[company.slug].append(company.parent)
		else:
			companydict[company.slug] = [company.name, company.parent]
	#foods = Food.objects.all()
	return render(request, 'directory/company_list.html', {'companies': companies, 'companydict': companydict})

"""def company_list(request):
	companies = Company.objects.all()
	return render(request, 'directory/company_list.html', {'companies': companies})"""

def company_entry(request, pk):
	company = get_object_or_404(Company, pk=pk)
	"""photos = CompanyPhoto.objects.filter(company=company)
	foods = Food.objects.filter(company=company)"""
	#import pdb; pdb.set_trace()
	return render(request, 'directory/company_entry.html', {'company': company})

def company_detail(request, string):
	companies = Company.objects.filter(slug = string)
	photos = []
	parents = []
	foods = []
	parentlist = []
	foodlist = []
	for company in companies:
		parents.append(company.parent)
		photos.extend(CompanyPhoto.objects.filter(company=company))
		foods.extend(Food.objects.filter(company=company))

	for parent in parents:
		if parent != None and parent.name not in parentlist:
			parentlist.append(parent.name)

	for food in foods:
		if food.name not in foodlist:
			foodlist.append(food.name)
	#import pdb; pdb.set_trace()
	return render(request, 'directory/company_detail.html', {'companies': companies, 'photos':photos, 'parentlist': parentlist, 'foodlist': foodlist})

@login_required
def company_new(request):
	if request.method == "POST":
		form = CompanyForm(request.POST)
		if form.is_valid():
			form.save(request.user)
			return redirect('directory.views.company_detail', pk=form.instance.pk)
	else:
		form = CompanyForm()
	return render(request, 'directory/edit.html', {'form': form})

@login_required
def company_edit(request, pk):
	company = get_object_or_404(Company, pk=pk)
	if request.method == "POST":
		form = CompanyForm(request.POST, instance=company)
		if form.is_valid():
			form.save(request.user)
			return redirect('directory.views.company_detail', pk=form.instance.pk)
	else:
		form = CompanyForm(instance=company)
	return render(request, 'directory/edit.html', {'form': form})

@login_required
def company_delete(request,pk):
	company = get_object_or_404(Company, pk=pk)
	if request.user == company.user:
		company.delete()
		return redirect('userprofile.views.user_profile')
# Create your views here.

@login_required
def company_photo_new(request):
	if request.method == "POST":
		form = CompanyPhotoForm(request.POST, request.FILES)
		if form.is_valid():
			form.save(request.user)
			return redirect('mainsite.views.home')
	else:
		form = CompanyPhotoForm()
	return render(request, 'directory/editimage.html', {'form':form})

@login_required
def company_photo_delete(request,pk):
	companyphoto = get_object_or_404(CompanyPhoto, pk=pk)
	if request.user == companyphoto.user:
		companyphoto.delete()
		return redirect('userprofile.views.user_profile')

@login_required
def food_photo_new(request):
	if request.method == "POST":
		form = FoodPhotoForm(request.POST, request.FILES)
		if form.is_valid():
			form.save(request.user)
			return redirect('mainsite.views.home')
	else:
		form = FoodPhotoForm()
	return render(request, 'directory/editimage.html', {'form':form})

@login_required
def food_photo_delete(request,pk):
	foodphoto = get_object_or_404(FoodPhoto, pk=pk)
	if request.user == foodphoto.user:
		foodphoto.delete()
		return redirect('userprofile.views.user_profile')
