from django.db import models

class Pastor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=20)
    pastoral_history = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"