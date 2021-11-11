from django.contrib import admin

# Register your models here.

from .models import Article, Driver, Constructor, Race

admin.site.register(Article)
admin.site.register(Driver)
admin.site.register(Constructor)
admin.site.register(Race)
