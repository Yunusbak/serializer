from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import AlbumView, ArtistView, SongView, ArtistView_new, SongView_new, AlbumView_new

urlpatterns = [
    # hamma malumotlar bor
    path('album', AlbumView.as_view(), name='album'),
    path('artist/', ArtistView.as_view(), name='artist'),
    path('song/', SongView.as_view(), name='song'),

    # faqat kerakli bolgan
    path('artist-1/', ArtistView_new.as_view(), name='artist-1'),
    path('song-1/', SongView_new.as_view(), name='song-1'),
    path('album-1/', AlbumView_new.as_view(), name='album-1'),

]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)