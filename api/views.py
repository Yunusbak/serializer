from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Song, Album, Artist
from .serializer import SongSerializer, AlbumSerializer, ArtistSerializer


class ArtistView(APIView):
    def get(self, request):

        search_query = request.GET.get('search', None)

        if search_query:
            artists = Artist.objects.filter(first_name__icontains=search_query) | Artist.objects.filter(last_name__icontains=search_query)
        else:
            artists = Artist.objects.all()

        serializer = ArtistSerializer(artists, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArtistDetailView(APIView):
    def get(self, request, id):
        artist = Artist.objects.get(id=id)
        serializer = ArtistSerializer(artist)
        return Response(serializer.data)
    def put(self, request, id):
        artist = Artist.objects.get(id=id)
        serializer = ArtistSerializer(instance=artist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        artist = Artist.objects.get(id=id)
        serializer = ArtistSerializer(instance=artist, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request,  id):
        artist = Artist.objects.get(id=id)
        artist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AlbumView(APIView):
    def get(self, request):
        search_query = request.GET.get('search', None)
        if search_query:
            queryset = Album.objects.filter(title__icontains=search_query)
        else:
            queryset = Album.objects.all()
        serializer = AlbumSerializer(queryset, many=True)
        data = serializer.data
        return Response(data=data)

    def post(self, request):
        serializer = AlbumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AlbumDetailView(APIView):
    def get(self, request, id):
        album = Album.objects.get(id=id)
        serializer = AlbumSerializer(album)
        return Response(serializer.data)
    def put(self, request, id):
        album = Album.objects.get(id=id)
        serializer = AlbumSerializer(instance=album, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request, id):
        album = Album.objects.get(id=id)
        serializer = AlbumSerializer(instance=album, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        album = Album.objects.get(id=id)
        album.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SongView(APIView):
    def get(self, request):
        search_query = request.GET.get('search', None)
        if search_query:
            queryset = Song.objects.filter(title__icontains=search_query) | Song.objects.filter(artist__first_name__icontains=search_query)
        else:
            queryset = Song.objects.all()

        serializer = SongSerializer(queryset, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class SongDetailView(APIView):
    def get(self, request, id):
        song = Song.objects.get(id=id)
        serializer = SongSerializer(song)
        return Response(serializer.data)

    def put(self, request, id):
        song = Song.objects.get(id=id)
        serializer = SongSerializer(instance=song, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        song = Song.objects.get(id=id)
        serializer = SongSerializer(instance=song, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, id):
        song = Song.objects.get(id=id)
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



