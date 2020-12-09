from django.contrib import admin

from .models import ArtikelModel, CommentModel
# Register your models here.


admin.site.register(ArtikelModel)
admin.site.register(CommentModel)
