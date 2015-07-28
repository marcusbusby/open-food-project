from django.shortcuts import render, get_object_or_404
from .models import Food, Company, FoodMap, CompanyPhoto, FoodPhoto
from django.contrib.auth.decorators import login_required
from .forms import FoodForm, CompanyForm, ComponentForm, CompanyPhotoForm, FoodPhotoForm
from django.shortcuts import redirect

def search(request):
	if request.method == "GET":
		search_text = request.GET['search_text']
	else: 
		search_text = ''

	foods = Food.objects.filter(name__contains=search_text)
	companies = Company.objects.filter(name__contains=search_text)


	# import pdb; pdb.set_trace()

	return render(request, 'directory/search.html', {'foods':foods, 'companies':companies})

def food_sort(request):
	if request.method == "GET":
		sort_value = request.GET['sort_value']

	foods = Food.objects.order_by(sort_value)

	# import pdb; pdb.set_trace()

	return render(request, 'directory/food_sort.html', {'foods':foods})

def food_list(request):
	foods = Food.objects.filter(edit=False)
	#foods = Food.objects.all()
	return render(request, 'directory/food_list.html', {'foods': foods})

def food_detail(request, pk):
	food = get_object_or_404(Food, pk=pk)
	contents = food.get_view_contents
	photos = FoodPhoto.objects.filter(food=food)
	foodmaps = FoodMap.objects.filter(target=food)
	"""food_dict = {}
	for foodmap in foodmaps:
		if foodmap.component not in food_dict:
			food_dict[foodmap.component]=[0,0]
	
	for foodmap in foodmaps:
		for food in food_dict:
			if foodmap.component == food.key:
				food_dict[foodmap.component][0] += foodmap.component.amount
				food_dict[foodmap.component][1] += 1 
	for key, value in food_dict.items()
		avg = value[0][0]/value[0][1]
		food_dict[key] = avg

	cleanfoodmaps = []
	for foodmap in foodmaps:
		if foodmap.edit = False:
			cleanfoodmaps += foodmap"""

	return render(request, 'directory/food_detail.html', {'food': food, 'foodmaps': foodmaps, "photos": photos})

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

def food_filter(request, pk):
	company = Company.objects.get(pk = pk)
	foods = Food.objects.filter(company=company)
	return render(request, 'directory/food_list.html', {'foods': foods})

def company_list(request):
	companies = Company.objects.all()
	return render(request, 'directory/company_list.html', {'companies': companies})

def company_detail(request, pk):
	company = get_object_or_404(Company, pk=pk)
	photos = CompanyPhoto.objects.filter(company=company)
	foods = Food.objects.filter(company=company)
	#import pdb; pdb.set_trace()
	return render(request, 'directory/company_detail.html', {'company': company, 'foods': foods, 'photos':photos})

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

#to do tomorrow

#change get_contents to return a list
#add links to templates that go back and forth between data
#ensure models methods are correct with carl
#add a function that gets the foods of a company
#add a function that calibrates the units of 
#change base unit to choice area
