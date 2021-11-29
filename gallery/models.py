from django.db import models
from PIL import Image
import PIL.Image as Image 

# Create your models here.

class Photographer(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)

    def __str__(self):
      return self.first_name

    class meta:
        ordering = ['name']

    def save_photographer(self):
        self.save()

class Location(models.Model):
    title = models.CharField(max_length =50)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def update_location(self, update):
        self.title = update
        self.save()

    @classmethod
    def get_location_id(cls, id):
        location_id = Location.objects.get(pk = id)
        return location_id

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length =50)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def update_category(self, update):
        self.title = update
        self.save()

    @classmethod
    def get_category_id(cls, id):
        category_id = Category.objects.get(pk = id)
        return category_id

    def __str__(self):
        return self.title

class Image(models.Model):
    title = models.CharField(max_length =60)
    photograph = models.ForeignKey(Photographer,on_delete=models.CASCADE,)
    pub_date = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    photo_image = models.ImageField(upload_to = 'images/', blank=True, null=True)
    
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_image(cls, id ,title,description, photograph, location, category):
        update = cls.objects.filter(id = id).update(title = title,description = description,photograph = photograph,location = location,category = category)
        return update

    @classmethod
    def get_all_images(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def get_image_id(cls,id):
        photo_id = cls.objects.filter(id= id).all()
        return photo_id

    @classmethod
    def filter_image_by_location(cls,location):
        photo_location = Image.objects.filter(location__title__icontains=location)
        return photo_location

    @classmethod
    def search_images_by_category(cls,category):
        photo_category = Image.objects.filter(category__title__icontains=category)
        return photo_category
    
    def search_by_title(cls,search_term):
        gallery = Image.objects.filter(title__icontains=search_term)
        return gallery


    def __str__(self):
        return self.title
