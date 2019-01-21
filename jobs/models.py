from django.db import models

# Create your models here.
# python object being saved in database


class Job(models.Model):
    image = models.ImageField(upload_to="images/")
    summary = models.CharField(max_length=200)

    def __str__(self):
        return self.summary[:10]
