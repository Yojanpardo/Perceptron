"""perceptronweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from perceptronweb import views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
    	route='',
        view=views.MainView.as_view(),
        name='home'
    ),
    path(
    	route='andpage/',
        view=views.AndView.as_view(),
        name='andpage'
    ),
        path(
    	route='',
        view=views.NandView.as_view(),
        name='nand'
    ),
    path(
    	route='',
        view=views.OrView.as_view(),
        name='or'
    ),
]
