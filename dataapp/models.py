from django.db import models

# Create your models here.

class entry(models.Model):

    name = models.CharField(max_length=200)

    class Meta:
        db_table = 'users'