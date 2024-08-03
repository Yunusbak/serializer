
from django.db import models
from .helpers import SaveMediaFiles
# Create your models here.
class Artist(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.get_full_name()}'

class Album(models.Model):
    objects = None
    title = models.CharField(max_length=50)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=SaveMediaFiles.image_save_album)

    def __str__(self):
        return f'{self.title}'


class Song(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to=SaveMediaFiles.image_save_song)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'