from django.contrib import admin
from gallery.models import Category, Image, Location, Photographer


# Register your models here.
admin.site.register(Photographer)
admin.site.register(Image)
admin.site.register(Location)
admin.site.register(Category)