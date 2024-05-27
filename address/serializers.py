from rest_framework import serializers
from .models import Province, City


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model= City
        fields = '__all__'       


class ProvinceSerializer(serializers.ModelSerializer):
    cities_of_province = CitySerializer(
        many= True, 
        source= "get_cities", 
        read_only = True,
    )
    class Meta:
        model= Province
        fields = '__all__'  





