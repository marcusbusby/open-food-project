from django.forms import widgets
from rest_framework import serializers
from directory.models import Company, Food, FoodMap, PointOfSale
from django.contrib.auth.models import User

class PointOfSaleSerializer(serializers.ModelSerializer):

	class Meta:
		model = PointOfSale
		fields = ('seller', 'latitude', 'longitude',)
		
class FoodSerializer(serializers.ModelSerializer):
	user = serializers.ReadOnlyField(source='user.username')
	company = serializers.SlugRelatedField(queryset = Company.objects.all(), slug_field='name')
	pointofsale = PointOfSaleSerializer()

	class Meta:
		model = Food
		fields = ('id', 'name', 'entry_time', 'company', 'user', 'pointofsale',)


class CompanySerializer(serializers.ModelSerializer):
	user = serializers.ReadOnlyField(source='user.username')
	foods = serializers.SlugRelatedField(many=True, queryset = Food.objects.all(), slug_field='name')
	parent = serializers.SlugRelatedField(queryset = Company.objects.all(), slug_field='name')

	class Meta:
		model = Company
		fields = ('id', 'name', 'entry_time', 'foods', 'parent', 'user',)


class FoodMapSerializer(serializers.ModelSerializer):
	user = serializers.ReadOnlyField(source='user.username')
	target = FoodSerializer()
	component = FoodSerializer()

	class Meta:
		model = FoodMap
		fields = ('id', 'target', 'component', 'entry_time', 'amount', 'unit', 'base_amount', 'base_unit', 'citation',  'user',)

class UserSerializer(serializers.ModelSerializer):
	companies = serializers.SlugRelatedField(many=True, queryset = Company.objects.all(), slug_field='name')
	foods = serializers.SlugRelatedField(many=True, queryset = Food.objects.all(), slug_field='name')
	foodmaps = serializers.PrimaryKeyRelatedField(many=True, queryset = FoodMap.objects.all())

	class Meta:
		model = User
		fields = ('id', 'username', 'companies', 'foods', 'foodmaps')