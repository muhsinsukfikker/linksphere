from django.contrib import admin

# Register your models here.
from social.models import   Posts,Stories

admin.site.register(Posts)
admin.site.register(Stories)