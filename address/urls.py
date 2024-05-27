from django.urls import path
from .views import(
    CityListCreateAPIView,
    CityRetrieveUpdateDestroyAPIView,
    ProvinceListCreateAPIView,
    ProvinceRetrieveUpdateDestroyAPIView
) 


urlpatterns = [
    path('cities/', CityListCreateAPIView.as_view(), name= "cities-list-create"),
    path('cities/<pk>/', CityRetrieveUpdateDestroyAPIView.as_view(), name= "cities-retrieve-update-destroy"),
    path('provinces/', ProvinceListCreateAPIView.as_view(), name= "provices-list-create"),
    path('provinces/<pk>/', ProvinceRetrieveUpdateDestroyAPIView.as_view(), name= "provices-retrieve-update-destroy" ),
]
