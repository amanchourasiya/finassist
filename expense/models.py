from django.db import models

# Create your models here.

class Expense(models.Model):
    # Category of expense e.g rent , grocery, food etc
    category = models.CharField(max_length=30)

    # Decription of expense
    description = models.CharField(max_length=100)

    # Amount of expense
    amount = models.IntegerField()
    