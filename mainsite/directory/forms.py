from django import forms

from .models import Food, Company

class FoodForm(forms.ModelForm):

	class Meta:
		model = Food
		fields = ['name', 'base_amount', 'base_unit', 'components', 'company']

class CompanyForm(forms.ModelForm):

	class Meta:
		model = Company
		fields = ['name', 'parent']