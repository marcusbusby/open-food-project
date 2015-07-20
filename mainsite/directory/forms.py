from django import forms

from .models import Food, Company, FoodMap

class FoodForm(forms.ModelForm):

	class Meta:
		model = Food
		fields = ['name', 'base_amount', 'base_unit', 'company']


class CompanyForm(forms.ModelForm):

	class Meta:
		model = Company
		fields = ['name', 'parent']

class ComponentForm(forms.ModelForm):

	class Meta:
		model = FoodMap
		fields = ['target', 'component', 'amount', 'unit']