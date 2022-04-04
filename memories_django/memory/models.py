from io import BytesIO
from pickle import TRUE
from PIL import Image

from django.core.files import File
from django.db import models
from django.contrib.auth.models import User

class Memory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)                     
    slug = models.SlugField()
    species = models.CharField(null=True, max_length=100)
    weight  = models.FloatField(default=0)
    length = models.FloatField(default=0)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='uploads/', blank=True, null=True)
    timestamp = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ('-timestamp',)                         # ordering = ('-timestamp',)
        
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'

    def get_photo(self):
        if self.photo:
            return 'http://127.0.01:8000' + self.photo.url
        else:
            if self.image:
                self.photo = self.make_photo(self.image)
                self.save()
                return 'http://127.0.01:8000' + self.photo.url
            else:
                return '/static/images/no-image.png'

    def make_photo(self, image, size=(140, 140)):                       # size=(140, 140)
        img = Image.open(image)
        img.convert('RGB')
        img.photo(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=80)

        photo = File(thumb_io, name=image.name)

        return photo