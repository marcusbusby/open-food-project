from django.shortcuts import render, get_object_or_404
from .models import Food, Company

def food_list(request):
	foods = Food.objects.all()
	return render(request, 'directory/food_list.html', {'foods': foods})

def food_detail(request, pk):
	food = get_object_or_404(Food, pk=pk)
	return render(request, 'directory/food_detail.html', {'food': food})

def company_list(request):
	companies = Company.objects.all()
	return render(request, 'directory/company_list.html', {'companies': companies})

def company_detail(request, pk):
	company = get_object_or_404(Company, pk=pk)
	return render(request, 'directory/company_detail.html', {'company': company})

# Create your views here.
