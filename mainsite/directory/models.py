from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

GRAMS = 'g'
KILOGRAMS = 'kg'
FLUID_OUNCES = 'fl oz'
OUNCES = 'oz'
UNIT_OF_MEASURE = ((GRAMS, 'g'), (KILOGRAMS, 'kg'), (FLUID_OUNCES,'fl oz'), (OUNCES, 'oz'))

class Food(models.Model):
	id = models.AutoField(primary_key = True)
	name = models.CharField(max_length = 30)
	components = models.ManyToManyField("self", through='FoodMap', symmetrical=False, related_name='component+', null = True, blank = True)
	company = models.ForeignKey('Company', null=True, blank=True)
	user = models.ForeignKey(User)

	def get_contents(self):
		content_list = []
		foodmaps = FoodMap.objects.filter(target = self)
		for foodmap in foodmaps:
			content_list.append(foodmap.component)
		return content_list

	def get_view_contents(self):
		content_dict = {}
		foodmaps = FoodMap.objects.filter(target = self)
		for foodmap in foodmaps:
			content_dict[foodmap.component] = [foodmap.component.name, foodmap.component.pk, foodmap.amount, foodmap.unit.__str__()]
		return content_dict

	def __unicode__(self):
		return '%s' % self.name

class FoodMap(models.Model):
	target = models.ForeignKey(Food, related_name="target")
	component = models.ForeignKey(Food, related_name="component")
	amount = models.IntegerField()
	unit = models.CharField(max_length = 10, choices=UNIT_OF_MEASURE)
	base_amount = models.IntegerField()
	base_unit = models.CharField(max_length=10, choices=UNIT_OF_MEASURE)
	citation = models.CharField(max_length=200)
	user = models.ForeignKey(User)


class Company(models.Model):
	id = models.AutoField(primary_key = True)
	name = models.CharField(max_length = 30)
	parent = models.ForeignKey('self', null=True, blank=True)
	user = models.ForeignKey(User)

	def __unicode__(self):
		return '%s' % self.name

	def get_subsidiaries(self, include_self=False):
		subs = []
		if include_self:
			subs.append(self)
		for sub in Company.objects.filter(parent = self):
			subs.append(sub.get_subsidiaries(include_self=True))
		return subs

	def get_lineage(self):
		company = self
		while company.parent is not None:
			company = company.parent
		lineage = [company]
		addendum = company.get_subsidiaries()
		lineage.append(addendum)
		return lineage

	def get_ancestor(self):
		company = self
		while company.parent is not None:
			company = company.parent
		return company
		

"""base_amount = models.IntegerField()
	base_unit = models.CharField(max_length = 10, choices=UNIT_OF_MEASURE)"""




# Create your models here.
