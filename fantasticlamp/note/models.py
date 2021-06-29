from django.db import models

# Create your models here.


class Inscription(models.Model):
    title = models.CharField(max_length=64)
    content = models.CharField(max_length=300)
    date_created = models.DateTimeField()

    def __str__(self):
        return self.title
