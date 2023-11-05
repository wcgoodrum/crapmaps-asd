from django.db import models

# Create your models here.
from django.db import models

class Bathroom(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=12, decimal_places=9)
    longitude = models.DecimalField(max_digits=12, decimal_places=9)

    def __str__(self):
        return self.name
    
class Review(models.Model):
    id = models.AutoField(primary_key=True)
    bathroom = models.ForeignKey(Bathroom, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.CharField(max_length=500)
    approved_status = models.BooleanField(default=False)

    def __str__(self):
        return self.comment