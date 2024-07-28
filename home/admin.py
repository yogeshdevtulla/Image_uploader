from django.contrib import admin
from .models import image
# Register your models here.

class imageadmin(admin.ModelAdmin):
    list_display=['id','First_name','Last_name','phone_number','photo','date']
admin.site.register(image,imageadmin)  # or @admin.register(image)