from django.db import models

# Create your models here.

from django.db import models

class Municipality(models.Model):
    name  = models.CharField(max_length=100)
    city  = models.CharField(max_length=100)
    rfc = models.CharField(max_length=13)
    government = models.CharField(max_length=50)
    status = models.CharField(max_length=10, default='active')

    class Meta:
        db_table = 'smm_municipality'  # sure it matches the table name

    def __str__(self):
        return self.name