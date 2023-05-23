from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class ExtendUser(AbstractUser):
    email = models.EmailField(blank=False, max_length=255, verbose_name="email")
    
    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    
    
class Job(models.Model):
    job_id = models.CharField(max_length=50, unique=True)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.job_id} ({self.status})"