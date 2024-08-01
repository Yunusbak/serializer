
import uuid

class SaveMediaFiles(object):
    def image_save_album(instance, filename):
        image = filename.split('.')[-1]
        return f"album-img/{uuid.uuid4()}.{image}"

    def image_save_song(instance, filename):
        image = filename.split('.')[-1]
        return f"song-img/{uuid.uuid4()}.{image}"