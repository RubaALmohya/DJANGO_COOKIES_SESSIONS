from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    release_date = models.IntegerField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    name = models.CharField(max_length=124)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
