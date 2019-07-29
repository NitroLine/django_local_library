from django.db import models
import os
# Create your models here.
def get_image_path(instance, filename):
    return os.path.join('images', str(instance.id), filename)

class Book(models.Model):
    title = models.CharField(max_length=150,db_index=True)
    author = models.CharField(max_length=150,db_index=True)
    discr= models.TextField(blank=True,db_index=True)
    profile_image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    date_pub=models.DateTimeField(auto_now_add=True)
    count=models.IntegerField()


    def __str__(self):
        return str(self.title)
