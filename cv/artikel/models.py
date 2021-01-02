from django.db import models

#import slugify
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save
# from django.dispatch import receiver
from .utils import unique_slug_generator


# Create your models here.

class ArtikelModel(models.Model):
    # id
    judul = models.CharField(max_length=225)
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    slug = models.SlugField(max_length=100, blank=True, null=True, unique=True)
    isi = models.TextField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.judul 


    
    # def save(self, *args, **kwargs):
    #     print("save 1")
    #     super(ArtikelModel, self).save(*args, **kwargs)
    #     if not self.slug:
    #         self.slug = slugify(self.judul)+"-"+str(self.id)
    #         print("save 2")
    #         self.save()
        
    
    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.judul)
    #     super(ArtikelModel, self).save(*args, **kwargs)



    # @receiver(pre_save, sender=ArtikelModel)
    def pre_save_receiver(sender, instance, *args, **kwargs):
        print('sebelum')
        # print(instance.create_at)
        if not instance.slug:
            instance.slug = unique_slug_generator(instance)

    # def post_save_receiver(sender, instance, *args, **kwargs):
    #     if not instance.slug:
    #         instance.slug = unique_slug_generator(instance)
    #         instance.save()

    pre_save.connect(pre_save_receiver, )

    # post_save.connect(post_save_receiver)


        


    class Meta:
        ordering = ["-create_at", "-update_at"]


# comment models
class CommentModel(models.Model):
    judul = models.ForeignKey(ArtikelModel, on_delete=models.CASCADE, related_name="comment")
    name = models.CharField(max_length=50, null=True)
    content = models.TextField(null=True, blank=True)
    create_data = models.DateTimeField(auto_now_add=True)
















