from django.db import models

class Wedding(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    image = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



class Guest(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    wedding = models.ForeignKey(Wedding, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
