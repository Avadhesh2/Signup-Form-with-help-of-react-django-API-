from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    date_of_birth = models.DateField()
    password = models.CharField(max_length=255)
    confirm_password = models.CharField(max_length=255)

    def __str__(self):
        return self.name
