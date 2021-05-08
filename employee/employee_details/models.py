from django.db import models

# Create your models here.


class EmployeeDetails(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    email_id = models.CharField(max_length=30)
    age = models.CharField(max_length=20)

