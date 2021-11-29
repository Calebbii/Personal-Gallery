from django.test import TestCase

from gallery.views import images
from .models import Image, Location, Category, Photographer
# Create your tests here.

class ImageTestClass(TestCase):
    def setUp(self):
        self.photograph = Photographer(first_name="Caleb")
        self.photograph.save_photographer()

        self.category = Category(title="wildlife")
        self.category.save_category()

        self.location = Location(title="Nairobi")
        self.location.save_location()

        self.image = Image(title='Lion',photograph= self.photograph,location=self.location, category=self.category)
        self.image.save_image()
    

    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))

    def tearDown(self):
        self.image.delete_image()
        self.category.delete_category()
        self.location.delete_location()

    def test_save_method(self):
        self.image.save_image()
        images  = Image.objects.all()
        self.assertTrue(len(images)>0)

    def test_get_all_images(self):
        images = Image.get_all_images()
        self.assertTrue(len(images)>0)

    def test_get_photo_id(self):
        images= Image.get_image_id(self.image.id)
        self.assertTrue(len(images) == 1)

    def test_search_by_category(self):
        images = Image.search_images_by_category('Travels')
        self.assertTrue(len(images)==0)

    def test_filter_by_location(self):
        images = Image.filter_image_by_location('Naivasha')
        print(images)
        self.assertTrue(len(images)==0)

    def test_update(self):
        category = Category.get_category_id(self.category.id)
        category.update_category('coding')
        category = Category.get_category_id(self.category.id)
        self.assertTrue(category.title == 'coding')

    def test_update_image(self):
            self.image.save_image()
            photo = Image.update_image( self.image.id, 'test update', 'my test',self.loc, self.cat)
            image_item = Image.objects.filter(id = self.photo.id)
            print(image_item)
            self.assertTrue(Image.name == 'test update')

class LocationTestCLass(TestCase):
    #Set up Method
    def setUp(self):
        self.location = Location(title="Nairobi")
        self.location.save_location()

    def test_instance(self):
        self.assertTrue(isinstance(self.location,Location))

    def test_save_method(self):
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_delete_method(self):
        self.location.save_location()
        self.location.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)

    def test_update(self):
        location = Location.get_location_id(self.location.id)
        location.update_location('Nairobi')
        location = Location.get_location_id(self.location.id)
        self.assertTrue(location.title == 'Nairobi')

class CategoryTestClass(TestCase):
    # Set up Method
    def setUp(self):
        self.category = Category(title="nature")
        self.category.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_method(self):
        self.category.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0)

    def test_delete_method(self):
        self.category.save_category()
        self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)

    def test_update(self):
        category = Category.get_category_id(self.category.id)
        category.update_category('wildlife')
        category = Category.get_category_id(self.category.id)
        self.assertTrue(category.title == 'wildlife')