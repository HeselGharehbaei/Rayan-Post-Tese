from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from .serializers import (
    CitySerializer,
    ProvinceSerializer
)
from .models import(
    Province,
    City
)


class CityListCreateAPIView(ListCreateAPIView):
    queryset= City.objects.all()
    serializer_class= CitySerializer


class CityRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset= City.objects.all()
    serializer_class= CitySerializer


class ProvinceListCreateAPIView(ListCreateAPIView):
    queryset= Province.objects.all()
    serializer_class= ProvinceSerializer
    

class ProvinceRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset= Province.objects.all()
    serializer_class= ProvinceSerializer
