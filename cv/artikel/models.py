from django.db import models

#import slugify
from django.utils.text import slugify


# Create your models here.

class ArtikelModel(models.Model):
    # id
    judul = models.CharField(max_length=225)
    slug = models.SlugField(max_length=50, blank=True, null=True, unique=True)
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    isi = models.TextField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.judul)
        super(ArtikelModel, self).save(*args, **kwargs)



# comment models
class CommentModel(models.Model):
    judul = models.ForeignKey(ArtikelModel, on_delete=models.CASCADE, related_name="comment")
    name = models.CharField(max_length=50, null=True)
    content = models.TextField(null=True, blank=True)
    create_data = models.DateTimeField(auto_now_add=True)
















