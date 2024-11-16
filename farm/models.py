from django.db import models

# Create your models here.
class Pictures(models.Model):
    picture = models.ImageField(upload_to='images/')
    message = models.TextField()
    description = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description
    

class Testimonials(models.Model):
    picture = models.ImageField(upload_to='testimonials/')
    message = models.TextField()
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Blog(models.Model):
    date = models.DateField()
    picture = models.ImageField(upload_to='blogs/')
    name = models.CharField(max_length=255)
    description = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name
    
class Team(models.Model):
    picture = models.ImageField(upload_to='team/')
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    facebook = models.URLField()
    twitter = models.URLField()
    linkedin = models.URLField()

    def __str__(self):
        return self.name