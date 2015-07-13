from django.shortcuts import render
from .models import Food

def food_list(request):
	foods = Food.objects.all()
	return render(request, 'directory/food_list.html', {'foods': foods})
# Create your views here.
