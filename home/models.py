from django.db import models

# Create your models here.
class image(models.Model):
    First_name=models.CharField(max_length=20, null=True, blank=True)
    Last_name=models.CharField(max_length=20,null=True, blank=True)
    phone_number=models.IntegerField(null=True, blank=True)
    photo=models.ImageField( upload_to='myimage')#, height_field=None, width_field=None, max_length=None
    date=models.DateTimeField(auto_now_add=True)