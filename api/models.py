from django.db import models

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    about = models.TextField(max_length=2000)
    type = models.CharField(max_length=200, choices=[[1, 'Public'], [2, 'Private'], [3, 'Non-Profit']])
    added_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name + self.location

class Employee(models.Model):
    POSITION_CHOICES = [
        ('Manager', 'Manager'),
        ('Developer', 'Developer'),
        ('Accountant', 'Accountant'),
    ]

    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    about = models.TextField()
    position = models.CharField(max_length=200, choices=POSITION_CHOICES)

    
    company = models.ForeignKey(Company, on_delete=models.CASCADE)