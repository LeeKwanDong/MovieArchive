"""Archive URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from ArchiveApp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    #Main
    path('', views.Main),
    path("review/", views.Review),
    path("request/", views.Request), 
    
    #Register
    path("register/", views.Register), 
    path("registerok/", views.RegisterOK),
    path("login/", views.Login), 

    #CRUD
    path("moviesinsert/", views.MoviesInsert), 
    path("moviesinsertok/", views.MoviesInsertOK),
    path("moviesupdate/", views.MoviesUpdate), 
    path("moviesupdateok/", views.MoviesUpdateOK),  
    path("reviewinsert/", views.ReviewInsert),
    path("reviewinsertok/", views.ReviewInsertOK),
    path("reviewupdate/", views.ReviewUpdate), 
    path("reviewupdateok/", views.ReviewUpdateOK),
    path("delete/", views.Delete)
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
