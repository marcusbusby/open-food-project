from django.db import models
from django.utils import timezone



class Food(models.Model):
	id = models.AutoField(primary_key = True)
	name = models.CharField(max_length = 30)
	base_amount = models.IntegerField()
	base_unit = models.CharField(max_length = 10)
	components = models.ManyToManyField("self", through='FoodMap', symmetrical=False, related_name='component+', null = True, blank = True)
	company = models.ForeignKey('Company', null=True, blank=True)

	def get_contents(self):
		content_dict = {}
		foodmaps = FoodMap.objects.filter(target = self)
		for foodmap in foodmaps:
			content_dict[foodmap.component.name] = foodmap.amount.__str__() + foodmap.unit.__str__()
		return content_dict

	def __unicode__(self):
		return '%s' % self.name

class FoodMap(models.Model):
	target = models.ForeignKey(Food, related_name="target")
	component = models.ForeignKey(Food, related_name="component")
	amount = models.IntegerField()
	unit = models.CharField(max_length = 10)


class Company(models.Model):
	id = models.AutoField(primary_key = True)
	name = models.CharField(max_length = 30)
	parent = models.ForeignKey('self', null=True, blank=True)

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
		

"""def get_food_contents(food):
	targetfood = Food.object.get(name = food)
	content_dict = {}
	foodmaps = FoodMap.objects.filter(target = targetfood)
	for foodmap in foodmaps:
		content_dict.append(key=foodmap.component.name, value=foodmap.component.amount)
	return content_dict"""




# Create your models here.
