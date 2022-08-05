
from django.conf import settings
from django.contrib import admin
from django.urls import path
from testing.pages import AboutMe, Contact, HomePage
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , HomePage),
    path('about' , AboutMe) ,
    path('contact' , Contact ) 
]


if settings.DEBUG :

    urlpatterns = urlpatterns + static(settings.STATIC_URL , document_root = settings.STATIC_ROOT) 
    # urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)