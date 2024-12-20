from django.db import models

# Create your models here.
class creature(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=250)
    description = models.TextField()
    mythology = models.CharField(max_length=250)
    region = models.CharField(max_length=250)
    ref_link = models.CharField(max_length=250)

class ticket(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=250)
    description = models.TextField()
    mythology = models.CharField(max_length=250)
    region = models.CharField(max_length=250)
    ref_link = models.CharField(max_length=250, default='#')
    status = models.CharField(max_length=50)
    user = models.EmailField(max_length=250)
    message = models.TextField(default='')
