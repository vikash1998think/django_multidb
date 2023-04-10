from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Contract(models.Model):
    name = models.CharField("Contract Name", max_length=100, db_index=True)
    description = models.CharField("Contract Description", max_length=255, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="contracts")
    data = models.CharField(max_length=200, null=True, blank=True, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
    