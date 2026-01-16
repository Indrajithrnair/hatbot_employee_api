from django.db import models

# Create your models here.

class Employee(models.Model):

    DEPARTMENTS = (
        ("HR", "HR"),
        ("ENGINEERING", "ENGINEERING"),
        ("SALES", "SALES")
    )

    ROLES = (
        ("MANAGER", "MANAGER"),
        ("DEVELOPER", "DEVELOPER"),
        ("ANALYST", "ANALYST")
    )

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=20, choices=DEPARTMENTS, blank=True, null=True)
    role = models.CharField(max_length=20, choices=ROLES, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

