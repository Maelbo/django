from django.db import models
from datetime import datetime
# Create your models here.
from django.db import models

class Machine(models.Model):
    
    TYPE = (
        ('PC', ('PC - Run windows ')),
        ('Mac ', ('MAc - Run MacOS ')),
        ('Serveur ', ('Serveur - Simple Server to deploy virtual machines ')) ,
        ('Switch ', ('Switch - To maintains and connect servers ')),
    )
    
    id = models.AutoField(
                    primary_key=True,
                    editable=False)
    nom= models.CharField(
                max_length= 6)

    maintenanceDate = models.DateField ( default = datetime.now ())
    mach = models.CharField ( max_length =32 , choices =TYPE , default ='PC')
    
class Personnel(models.Model):
    id = models.AutoField(
                    primary_key=True,
                    default=False)
    nom = models.CharField(
                        max_length=20)
    prenom = models.CharField(
                        max_length=20)
    

