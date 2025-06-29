from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class User(AbstractUser):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='users')

class Kudos(models.Model):
    giver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='kudos_given')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='kudos_received')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.giver} -> {self.receiver}: {self.message[:20]}"