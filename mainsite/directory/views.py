from django.shortcuts import render, get_object_or_404
from .models import Food, Company
from .forms import FoodForm, CompanyForm
from django.shortcuts import redirect

def food_list(request):
	foods = Food.objects.all()
	return render(request, 'directory/food_list.html', {'foods': foods})

def food_detail(request, pk):
	food = get_object_or_404(Food, pk=pk)
	return render(request, 'directory/food_detail.html', {'food': food})

def food_new(request):
	if request.method == "POST":
		form = FoodForm(request.POST)
		if form.is_valid():
			food = form.save(commit=False)
			food.save()
			return redirect('directory.views.food_detail', pk=food.pk)
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
			company = form.save(commit=False)
			company.save()
			return redirect('directory.views.company_detail', pk=company.pk)
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

#add links to templates that go back and forth between data
#ensure models methods are correct with carl
#make sure forms work
#add a function that gets the foods of a company
#add a function that calibrates the units of 
#change base unit to choice area
