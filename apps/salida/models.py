from django.db import models


# Create your models here.
class Post(models.Model):
    nombre = models.CharField(max_length=100)
    categoria=models.TextField(max_length=500)
    cantidad=models.IntegerField()
    create_at=models.DateTimeField(auto_now_add=True)
    
    def __srt__(self):
        return self