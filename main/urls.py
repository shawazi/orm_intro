"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app.views import home, GenreView, GenreDetailView, ArtistView, ArtistDetailView, AlbumView, AlbumDetailView, SongView, SongDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', home),
    path('api/genre/', GenreView.as_view()),
    path('api/genre/<int:pk>/', GenreDetailView.as_view()),
    path('api/artist/', ArtistView.as_view()),
    path('api/artist/<int:pk/', ArtistDetailView.as_view()),
    path('api/album/', AlbumView.as_view()),
    path('api/album/<int:pk/', AlbumDetailView.as_view()),
    path('api/song/', SongView.as_view()),
    path('api/song/<int:pk/', SongDetailView.as_view()),
    
]