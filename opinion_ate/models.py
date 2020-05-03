from django.db import models

# Create your models here.
class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'author'
         


class Movie(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    score = models.IntegerField()
    author = models.ForeignKey(Author, on_delete = models.CASCADE)

    class Meta:
        managed = False
        db_table = 'movie'
