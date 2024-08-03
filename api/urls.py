from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import AlbumView, ArtistView, SongView, ArtistDetailView, AlbumDetailView, SongDetailView

urlpatterns = [

    #artist
    path('artist/', ArtistView.as_view(), name='artist'),
    path('artist/<int:id>/', ArtistDetailView.as_view(), name='artist-detail'),
    #albom
    path('album', AlbumView.as_view(), name='album'),
    path('album/<int:id>/', AlbumDetailView.as_view(), name='album-detail'),
    #song
    path('song/', SongView.as_view(), name='song'),
    path('song/<int:id>/', SongDetailView.as_view(), name='song-detail'),

]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

