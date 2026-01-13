from django.db import models

class Cars(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    year = models.PositiveIntegerField(blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    mileage = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.brand} {self.name} ({self.year})"
