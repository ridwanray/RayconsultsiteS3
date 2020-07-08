from django.db import models

class Contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=70)
    subject=models.CharField(max_length=60)
    content=models.TextField()

    def __str__(self):
        return self.name