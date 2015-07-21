from django import forms

from .models import Food, Company, FoodMap

class FoodForm(forms.ModelForm):

	class Meta:
		model = Food
		fields = ['name', 'company']
		exclude = ('user',)

	def save(self, user, commit=True):
		food = forms.ModelForm.save(self, commit=False)
		food.user = user
		if commit:
			food.save()
		return food


class CompanyForm(forms.ModelForm):

	class Meta:
		model = Company
		fields = ['name', 'parent']
		exclude = ('user',)

	def save(self, user, commit=True):
		company = forms.ModelForm.save(self, commit=False)
		company.user = user
		if commit:
			company.save()
		return company

class ComponentForm(forms.ModelForm):

	class Meta:
		model = FoodMap
		fields = ['target', 'component', 'amount', 'unit', 'base_amount', 'base_unit', 'citation']
		exclude = ('user',)

	def save(self, user, commit=True):
		component = forms.ModelForm.save(self, commit=False)
		component.user = user
		if commit:
			component.save()
		return component