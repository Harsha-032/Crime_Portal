from django.db import models

# Create your models here.

class wantedlist(models.Model):
    image = models.ImageField(upload_to='static/')
    name = models.CharField(max_length=20)
    dob = models.DateField()
    placeofbirth = models.CharField(max_length=20)
    hair = models.CharField(max_length=20)
    eyes = models.CharField(max_length=20)
    height = models.CharField(max_length=20)
    weight = models.CharField(max_length=20)
    sex = models.CharField(max_length=20)
    occupation = models.CharField(max_length=20)
    nationalaity = models.CharField(max_length=20)
    scarsandmarks = models.CharField(max_length=20)
    caution = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class safe(models.Model):
    From = models.CharField(max_length=20)
    precaution = models.TextField()

    def __str__(self):
        return self.From


    