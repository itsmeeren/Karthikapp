from django.db import models
from django.core.exceptions import ValidationError

class Contact(models.Model):
    name = models.CharField(max_length=500)
    email = models.EmailField(unique=True)  # unique is used because it should not crash the database
    phone = models.CharField(max_length=200, unique=True)
    desc = models.TextField()


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        try:
            super().save(*args, **kwargs)
        except ValidationError as e:

            print(f"Validation Error: {e}")


from django.db import models

from django.db import models

class ImageModel(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    video = models.FileField(upload_to='videos/', null=True, blank=True)


    def __str__(self):
        return self.title
    # to return the title of the image





