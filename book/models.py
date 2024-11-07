from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=221)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="book_image/")
    downloads = models.PositiveIntegerField()
    file = models.FileField(upload_to='book_file/')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
