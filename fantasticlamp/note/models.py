from django.db import models

# Create your models here.


class Inscription(models.Model):
    title = models.CharField(max_length=64)
    desc = models.CharField(max_length=100, blank=True)
    content = models.TextField(max_length=300)
    date_created = models.DateTimeField()
    cover = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.title


class Images(models.Model):
    image = models.ImageField(upload_to='InscriptionImages')
    inscription = models.ForeignKey(Inscription, on_delete=models.CASCADE)
    image_text = models.CharField(max_length=64)

    def __str__(self):
        return self.image_text
