from django.http.response import Http404
from django.shortcuts import get_object_or_404, render
from gallery.models import Image, Location
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def home(request):
    return render(request,'home.html')

def images(request):
  images = Image.get_all_images()
  location = Location.objects.all()
  return render(request,'photos.html',{'images':images, 'location':location})

def detail(request,image_id):
  locations = Location.objects.all()

  try:
    images = get_object_or_404(Image, pk = image_id)
  except ObjectDoesNotExist:
    raise Http404()
  return render(request, 'photo.html', {'images':images,"locations":locations})


def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "Please enter title to be searched"
        return render(request, 'search.html',{"message":message})




def filter_nature_images(request):
  try:
    images = Image.objects.filter(location =2)
  except ObjectDoesNotExist:
    raise Http404()
  return render(request, 'imageInfo.html', {'images':images})

def filter_food_drinks_images(request):
  try:
    photos = Image.objects.filter(location =1)
  except ObjectDoesNotExist:
    raise Http404()
  return render(request, 'imageInfo.html', {'images':images})

def filter_wildlife_images(request):
  try:
    images = Image.objects.filter(location =3)
  except ObjectDoesNotExist:
    raise Http404()
  return render(request, 'imageInfo.html', {'images':images})

def filter_travels_images(request):
  try:
    images = Image.objects.filter(location =4)
  except ObjectDoesNotExist:
    raise Http404()
  return render(request, 'imageInfo.html', {'images':images})