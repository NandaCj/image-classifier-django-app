from django.db import models
from django.conf import settings


class ImageDetails(models.Model):
    image = models.ImageField(db_column='image', upload_to=settings.IMG_DIR)
    image_name = models.CharField(db_column='image_name', max_length=255)

    def __str__(self):
        return str(self.image)