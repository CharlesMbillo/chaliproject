from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)  # You can use a better field type for phone numbers
    email = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

