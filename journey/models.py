from django.db import models
from django.conf import settings
from django.conf.urls.static import static
from django.urls import reverse


# Create your models here.
class Memory(models.Model):
    #print(settings.STATIC_URL)
    title= models.CharField(max_length=25,null=True,blank=True)
    place=models.CharField(max_length=20,null=True,blank=True)
    desc=models.TextField(default='write here',null=True,blank=True)
    image=models.ImageField(null=True,blank=True,upload_to='static/assets/img/')
    def __str__(self):
        return self.title
    def get_absolute_url(self):
            return reverse("memory:desc",kwargs={"id":self.id})        

