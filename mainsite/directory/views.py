from django.shortcuts import render, get_object_or_404
from .models import Food, Company, FoodMap
from .forms import FoodForm, CompanyForm, ComponentForm
from django.shortcuts import redirect

def home(request):
	return render(request, 'directory/home.html')

def food_list(request):
	foods = Food.objects.all()
	return render(request, 'directory/food_list.html', {'foods': foods})

def food_detail(request, pk):
	food = get_object_or_404(Food, pk=pk)
	contents = food.get_view_contents
	return render(request, 'directory/food_detail.html', {'food': food, 'contents': contents})

def food_new(request):
	if request.method == "POST":
		form = FoodForm(request.POST)
		if form.is_valid():
			form.save(request.user)
			return redirect('directory.views.food_detail', pk=form.instance.pk)
	else:
		form = FoodForm()
	return render(request, 'directory/edit.html', {'form': form})

def food_edit(request, pk):
	food = get_object_or_404(Food, pk=pk)
	if request.method == "POST":
		form = FoodForm(request.POST, instance=food)
		if form.is_valid():
			food = form.save(commit=False)
			food.save()
			return redirect('directory.views.food_detail', pk=food.pk)
	else:
		form = FoodForm(instance=food)
	return render(request, 'directory/edit.html', {'form': form})

def component_new(request):
	if request.method == "POST":
		form = ComponentForm(request.POST)
		if form.is_valid():
			form.save(request.user)
			return redirect('directory.views.food_list')
	else:
		form = ComponentForm()
	return render(request, 'directory/edit.html', {'form': form})


def food_filter(request, pk):
	company = Company.objects.get(pk = pk)
	foods = Food.objects.filter(company=company)
	return render(request, 'directory/food_list.html', {'foods': foods})

def company_list(request):
	companies = Company.objects.all()
	return render(request, 'directory/company_list.html', {'companies': companies})

def company_detail(request, pk):
	company = get_object_or_404(Company, pk=pk)
	foods = Food.objects.filter(company=company)
	return render(request, 'directory/company_detail.html', {'company': company, 'foods': foods})

def company_new(request):
	if request.method == "POST":
		form = CompanyForm(request.POST)
		if form.is_valid():
			form.save(request.user)
			return redirect('directory.views.company_detail', pk=form.instance.pk)
	else:
		form = CompanyForm()
	return render(request, 'directory/edit.html', {'form': form})

def company_edit(request, pk):
	company = get_object_or_404(Company, pk=pk)
	if request.method == "POST":
		form = CompanyForm(request.POST, instance=company)
		if form.is_valid():
			company = form.save(commit=False)
			company.save()
			return redirect('directory.views.company_detail', pk=company.pk)
	else:
		form = CompanyForm(instance=company)
	return render(request, 'directory/edit.html', {'form': form})
# Create your views here.

#to do tomorrow

#change get_contents to return a list
#add links to templates that go back and forth between data
#ensure models methods are correct with carl
#add a function that gets the foods of a company
#add a function that calibrates the units of 
#change base unit to choice area
