from django.db import models

# Create your models here.

class libraryDB(models.Model):
    Book_id=models.AutoField(primary_key=True)
    Book_Name=models.CharField(max_length=50)
    Book_author=models.CharField(max_length=50)
    Book_price=models.IntegerField()
