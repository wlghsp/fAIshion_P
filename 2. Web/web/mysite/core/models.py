from django.db import models


class Clothing(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='clothings/images/')

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)


class CoordinateClothing(models.Model):
    c_kind = models.IntegerField()
    c_image = models.ImageField(blank=True)
    c_url = models.CharField(max_length=200, blank=True)