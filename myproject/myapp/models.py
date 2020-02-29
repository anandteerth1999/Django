from django.db import models

# Create your models here.
class Student(models.Model):
    Name = models.CharField(max_length=20)
    USN = models.CharField(max_length=10)
    Class = models.CharField(max_length=3)
    Section = models.CharField(max_length=1)

    class Meta:
        db_table = "Student"

class Friends(models.Model):
    Name = models.CharField(max_length=20)
    FavNo = models.IntegerField()

    class Meta:
        db_table = "Friends"
