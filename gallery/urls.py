from django.conf.urls import include, url
from django.db.models.query_utils import PathInfo
from django.urls.conf import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.home,name = 'welcome'),
    path('photos/',views.images,name='allPhotos'),
    path('photos/',views.images,name='allVideo'),
    path('image/<int:image_id>',views.detail,name='image_item.detail'),
    path('nature/',views.filter_nature_images,name='nature'),
    path('food&drinks/',views.filter_food_drinks_images,name='foods'),
    path('wildlife/',views.filter_wildlife_images,name='wildlife'),
    path('travels/',views.filter_travels_images,name='travels'),
    path('search/',views.search_results, name='search_results'),
    path('details/',views.images,name='details'),
]
if settings.DEBUG:
    # urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # urlpatterns += url(r'',include('users.urls'))