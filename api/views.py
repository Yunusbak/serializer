from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Song, Album, Artist
from .serializer import SongSerializer, AlbumSerializer, ArtistSerializer, ArtistSerializer_new, SongSerializer_new, AlbumSerializer_new

class ArtistView(APIView):
    def get(self, request):
        queryset = Artist.objects.all()
        serializer = ArtistSerializer(queryset, many=True)
        return Response(data=serializer.data)

class AlbumView(APIView):
    def get(self, request):
        queryset = Album.objects.all()
        serializer = AlbumSerializer(queryset, many=True)
        data = serializer.data

        request_host = request.get_host()
        for item in data:
            if 'image' in item and item['image']:
                item['image'] = f"http://{request_host}{item['image']}"

        return Response(data=data)

class SongView(APIView):
    def get(self, request):
        queryset = Song.objects.all()
        serializer = SongSerializer(queryset, many=True)
        return Response(data=serializer.data)

class ArtistView_new(APIView):
    def get(self, request):
        queryset = Artist.objects.all()
        serializer = ArtistSerializer_new(queryset, many=True)
        return Response(data=serializer.data)

class AlbumView_new(APIView):
    def get(self, request):
        queryset = Album.objects.all()
        serializer = AlbumSerializer_new(queryset, many=True)
        data = serializer.data

        request_host = request.get_host()
        for item in data:
            if 'image' in item and item['image']:
                item['image'] = f"http://{request_host}{item['image']}"

        return Response(data=data)

class SongView_new(APIView):
    def get(self, request):
        queryset = Song.objects.all()
        serializer = SongSerializer_new(queryset, many=True)
        return Response(data=serializer.data)
