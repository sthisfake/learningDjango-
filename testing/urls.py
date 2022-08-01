
from django.contrib import admin
from django.urls import path
from testing.pages import AboutMe, HomePage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , HomePage),
    path('about' , AboutMe)
]
