from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Province, City
from rest_framework import status


class TestSetUp(APITestCase):


    def setUp(self) -> None: 
        """
        Create a new object for City and Province models.
        """
          
        self.province= Province.objects.create(name= 'Tehran')   
        self.city= City.objects.create(
            name= 'Tehran', 
            province= self.province
        ) 
        self.city_list_create_url= reverse('cities-list-create')
        self.city_detail_url= reverse(
            'cities-retrieve-update-destroy', 
            kwargs={'pk': self.city.id}
        ) 
        self.province_list_create_url= reverse('provices-list-create')         
        self.province_detail_url= reverse(
            'provices-retrieve-update-destroy', 
            kwargs={'pk': self.province.id}
        )

    def test_city_list_create(self):
        # test listing cities
        response= self.client.get(self.city_list_create_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['name'], 
            self.city.name
        )
        self.assertEqual(response.data[0]['province'], 
            self.province.id
        )
        # test creating a city
        self.city_data= {
            "name": "EslamShaher",
            "province": 1
        } 
        response= self.client.post(self.city_list_create_url, 
            data= self.city_data, 
            format= 'json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], self.city_data['name'])
        self.assertEqual(response.data['province'], self.city_data['province'])  
        self.assertEqual(City.objects.count(), 2)      

    def test_city_retrieve_update_destroy(self):
        # test retrieve a city
        response= self.client.get(self.city_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 
            self.city.name
        )
        self.assertEqual(response.data['province'], 
            self.province.id
        )        
        # test updating a city
        self.city_data= {
            "name": "ShahreRey",
            "province": 1
        }         
        response= self.client.put(self.city_detail_url, data= self.city_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.city_data['name'])
        self.assertEqual(response.data['province'], self.city_data['province'])
        # test deleting a city
        response= self.client.delete(self.city_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(City.objects.count(), 0) 

    def test_province_list_create(self):
        # test listing provinces
        response= self.client.get(self.province_list_create_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['name'], 
            self.province.name
        )
        self.assertEqual(response.data[0]['cities_of_province'][0]['name'], 
            self.city.name
        )
        # test creating a province
        self.province_data= {
            "name": "Golestan"
        } 
        response= self.client.post(self.province_list_create_url, 
            data= self.province_data, 
            format= 'json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], self.province_data['name'])
        self.assertEqual(response.data['cities_of_province'], [])  
        self.assertEqual(Province.objects.count(), 2)      

    def test_province_retrieve_update_destroy(self):
        # test retrieve a province
        response= self.client.get(self.province_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 
            self.province.name
        )
        self.assertEqual(response.data['cities_of_province'][0]['id'], 
            self.city.id
        )        
        # test updating a province
        self.province_data= {
            "name": "Mazandaran"
        }         
        response= self.client.put(self.province_detail_url, data= self.province_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.province_data['name'])
        self.assertEqual(response.data['cities_of_province'][0]['name'], 
            self.city.name
        )
        # test deleting a province
        response= self.client.delete(self.province_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Province.objects.count(), 0)      
