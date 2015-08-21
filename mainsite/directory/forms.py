from django import forms
from .models import Food, Company, FoodMap, CompanyPhoto, FoodPhoto, PointOfSale, Tag
from django.template.defaultfilters import slugify

class FoodForm(forms.ModelForm):

	class Meta:
		model = Food
		fields = ['name', 'company', 'tags']
		exclude = ('user', 'edit', 'entry_time', 'slug', 'pointofsale')

	def save(self, pos, user, present=False, commit=True):
		food = forms.ModelForm.save(self, commit=False)
		food.user = user
		food.pointofsale = pos
		food.slug = slugify(food.name)
		if present:
			food.edit = True
		if commit:
			food.save()
		return food

class PointOfSaleForm(forms.ModelForm):

	class Meta:
		model = PointOfSale
		fields = ['latitude', 'longitude', 'seller', 'tags']
		exclude = ('user',)

	def save(self, user, commit=True):
		pos = forms.ModelForm.save(self, commit=False)
		pos.user = user
		#import pdb; pdb.set_trace()
		if commit:
			pos.save()
		return pos


class CompanyForm(forms.ModelForm):

	class Meta:
		model = Company
		fields = ['name', 'parent', 'tags']
		exclude = ('user', 'edit', 'entry_time', 'slug')

	def save(self, user, commit=True):
		company = forms.ModelForm.save(self, commit=False)
		company.user = user
		company.slug = slugify(company.name)
		if commit:
			company.save()
		return company

class ComponentForm(forms.ModelForm):

	class Meta:
		model = FoodMap
		fields = ['target', 'component', 'amount', 'unit', 'base_amount', 'base_unit', 'citation']
		exclude = ('user', 'entry_time')

	def save(self, user, commit=True):
		component = forms.ModelForm.save(self, commit=False)
		component.user = user
		if commit:
			component.save()
		return component

class CompanyPhotoForm(forms.ModelForm):

	class Meta:
		model = CompanyPhoto
		fields = ['photo', 'title', 'company', 'tags']
		exclude = ('user', 'entry_time')

	def save(self, user, commit=True):
		companyphoto = forms.ModelForm.save(self, commit=False)
		companyphoto.user = user
		if commit:
			companyphoto.save()
		return companyphoto

class FoodPhotoForm(forms.ModelForm):

	class Meta:
		model = FoodPhoto
		fields = ['photo', 'title', 'food', 'tags']
		exclude = ('user', 'entry_time')

	def save(self, user, commit=True):
		foodphoto = forms.ModelForm.save(self, commit=False)
		foodphoto.user = user
		if commit:
			foodphoto.save()
		return foodphoto

class TagForm(forms.ModelForm):

	class Meta:
		model = Tag
		fields = ['name']

	def save(self, user, commit=True):
		tag = forms.ModelForm.save(self, commit=False)
		tag.user = user
		if commit:
			tag.save()
		return tag

