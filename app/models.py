from django.db import models

# Create your models here.
class blog (models.Model):
    title=models.CharField(max_length=50)
    body=models.TextField()
    email=models.EmailField()
    phone = models.IntegerField()
    def __str__(self):
        return self.title

