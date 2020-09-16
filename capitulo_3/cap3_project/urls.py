"""cap3_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path


from cap3_app import views


urlpatterns = [
    path('home/',views.home_page,name='home'),

    path('admin/', admin.site.urls),
    path('canelones/',views.canelones,name='canelones'),
    path('carbonara/',views.carbonara,name='carbonara'),
    path('ensaladilla_rusa/',views.ensaladilla_rusa,name='ensaladilla_rusa'),
    path('feijoada/',views.feijoada,name='feijoada'),
    path('flor_de_calabacin/',views.flor_de_calabacin,name='flor_de_calabacin'),
    path('Gazpacho/',views.Gazpacho,name='Gazpacho'),
    path('mafe/',views.mafe,name='mafe'),
    path('menu_infantil/',views.menu_infantil,name='menu_infantil'),
    path('pizza/',views.pizza,name='pizza'),
    path('Receta_Facil/',views.Receta_Facil,name='Receta_Facil'),
    path('sopa_de_noodles/',views.sopa_de_noodles,name='sopa_de_noodles'),

]
