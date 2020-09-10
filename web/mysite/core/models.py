from django.db import models


class Clothing(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='clothings/images/')

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)
