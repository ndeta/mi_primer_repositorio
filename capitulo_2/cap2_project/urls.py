from django.contrib import admin
from django.urls import path

from plantillas.views import home_page_view,ndeya_about,about_page_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home_page_view ,name='home'),

    path('about/', about_page_view,name='about'),

]
