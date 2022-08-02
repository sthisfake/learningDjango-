
from django.contrib import admin
from django.urls import path
from testing.pages import AboutMe, Contact, HomePage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , HomePage),
    path('about' , AboutMe) ,
    path('contact' , Contact ) 
]
