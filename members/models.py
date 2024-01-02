from django.db import models

# Create your models here.

class User(models.Model):
    NAMA = models.CharField(max_length=50)

    def _str_(self):
        return f"{self.NAMA}"