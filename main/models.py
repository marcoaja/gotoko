from django.db import models
import uuid
# Create your models here.
class Product(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField(max_length=100)
  price = models.IntegerField()
  description = models.TextField()
  category = models.CharField(max_length=50)
  stock = models.IntegerField()
  created_at = models.DateField(auto_now_add=True)