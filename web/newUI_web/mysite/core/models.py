from django.db import models
from django.contrib.auth.models import User





class Member(models.Model):
    # user와 1대1 매칭
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="member")
    name = models.CharField(max_length=10)



class Clothing(models.Model):
    owner = models.ForeignKey(
        Member, on_delete=models.SET_NULL, null=True, related_name="clothing")
    image = models.ImageField(upload_to='clothings/images/')



    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)


class CoordinateClothing(models.Model):
    c_kind = models.IntegerField()
    c_image = models.ImageField(blank=True)
    c_url = models.CharField(max_length=200, blank=True)