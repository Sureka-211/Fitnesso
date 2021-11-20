from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Mind)
admin.site.register(Image)
admin.site.register(cardio)
admin.site.register(dance)
admin.site.register(yoga)
admin.site.register(walk)
admin.site.register(filesupload)