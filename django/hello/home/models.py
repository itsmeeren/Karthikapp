from django.db import models
from django.core.exceptions import ValidationError

class Contact(models.Model):
    name = models.CharField(max_length=500)
    email = models.EmailField(unique=True)  # Ensure uniqueness for email
    phone = models.CharField(max_length=200, unique=True)  # Ensure uniqueness for phone
    desc = models.TextField()


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        try:
            super().save(*args, **kwargs)
        except ValidationError as e:
            # Handle the validation error, e.g., print a message or log it
            print(f"Validation Error: {e}")
            # You might want to raise a more user-friendly error or handle it differently based on your use case

