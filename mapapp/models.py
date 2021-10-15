from django.db import models

# Create your models here.
class maplist(models.Model):
    mapName=models.CharField(max_length=60,null=False)
    mapDesc=models.TextField(null=False)
    mapLat=models.CharField(max_length=20,null=False)
    mapLng=models.CharField(max_length=20,null=False)
    mapTel=models.CharField(max_length=20,null=False)
    mapAddr=models.CharField(max_length=60,null=False)

    def __str__(self):
        return self.mapName