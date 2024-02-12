from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.WatchList)
admin.site.register(models.StreamPlatform)
admin.site.register(models.Review)