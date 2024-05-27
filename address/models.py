from django.db import models


class Province(models.Model):
    name= models.CharField(max_length=50,)

    def get_cities(self):
        return self.cities.all()


class City(models.Model):
    name= models.CharField(max_length=50,)
    province= models.ForeignKey(
        "Province",
        on_delete=models.CASCADE,
        related_name="cities"
    )
