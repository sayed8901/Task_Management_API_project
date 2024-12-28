from django.db import models
from accounts.models import CustomUser

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="owned_projects")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} project"
