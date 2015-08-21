from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

GRAMS = 'g'
KILOGRAMS = 'kg'
MILLIGRAMS = 'mg'
FLUID_OUNCES = 'fl oz'
OUNCES = 'oz'
LITERS = 'L'
MILLILITERS = 'mL'
UNIT_OF_MEASURE = ((GRAMS, 'g'), (KILOGRAMS, 'kg'), (MILLIGRAMS, 'mg'), (FLUID_OUNCES,'fl oz'), (OUNCES, 'oz'), (LITERS, 'L'), (MILLILITERS, 'mL'))

class Food(models.Model):
	id = models.AutoField(primary_key = True)
	name = models.CharField(max_length = 30)
	components = models.ManyToManyField("self", through='FoodMap', symmetrical=False, related_name='component+', null = True, blank = True)
	company = models.ForeignKey('Company', null=True, blank=True, related_name='foods')
	user = models.ForeignKey('auth.User', related_name='foods')
	pointofsale = models.ForeignKey('PointOfSale', null=True, blank=True)
	edit = models.BooleanField(default=False)
	entry_time = models.DateTimeField(default = timezone.now)
	slug = models.SlugField(default='')
	tags = models.ManyToManyField('Tag', null=True, blank=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Food, self).save(*args, **kwargs)

	"""def get_contents(self):
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
		return content_dict"""

	def __str__(self):
		return '%s' % self.name

class FoodMap(models.Model):
	target = models.ForeignKey(Food, related_name="target")
	component = models.ForeignKey(Food, related_name="component")
	amount = models.IntegerField(null=True, blank=True)
	unit = models.CharField(max_length = 10, choices=UNIT_OF_MEASURE, null=True, blank=True)
	base_amount = models.IntegerField(null=True, blank=True)
	base_unit = models.CharField(max_length=10, choices=UNIT_OF_MEASURE, null=True, blank=True)
	citation = models.CharField(max_length=200)
	user = models.ForeignKey('auth.User', related_name='foodmaps')
	edit = models.BooleanField(default=False)
	entry_time = models.DateTimeField(default = timezone.now)

class Company(models.Model):
	id = models.AutoField(primary_key = True)
	name = models.CharField(max_length = 30)
	parent = models.ForeignKey('self', null=True, blank=True)
	user = models.ForeignKey('auth.User', related_name='companies')
	edit = models.BooleanField(default=False)
	entry_time = models.DateTimeField(default = timezone.now)
	slug = models.SlugField(null=True)
	tags = models.ManyToManyField('Tag', null=True, blank=True)

	def __str__(self):
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
		
class CompanyPhoto(models.Model):
	photo = models.ImageField(upload_to='photos')
	title = models.CharField(max_length=50)
	company = models.ForeignKey(Company)
	user = models.ForeignKey(User)
	entry_time = models.DateTimeField(default = timezone.now)
	tags = models.ManyToManyField('Tag', null=True, blank=True)

class FoodPhoto(models.Model):
	photo = models.ImageField(upload_to='photos')
	title = models.CharField(max_length=50)
	food = models.ForeignKey(Food)
	user = models.ForeignKey(User)
	entry_time = models.DateTimeField(default = timezone.now)
	tags = models.ManyToManyField('Tag', null=True, blank=True)

class PointOfSale(models.Model):
	latitude = models.DecimalField(max_digits=20, decimal_places=15)
	longitude = models.DecimalField(max_digits=20, decimal_places=15)
	seller = models.CharField(max_length=50)
	user = models.ForeignKey(User)
	tags = models.ManyToManyField('Tag', null=True, blank=True)

class Tag(models.Model):
	name = models.CharField(max_length=100)





# Create your models here.
