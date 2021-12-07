import os
from os.path import join

from django.conf import settings
from django.db import models


class Pet(models.Model):
    DOG = 'dog'
    CAT = 'cat'
    PARROT = 'parrot'
    UNKNOWN = 'unknown'

    PET_TYPES = (
        (DOG, 'Dog'),
        (CAT, 'Cat'),
        (PARROT, 'Parrot'),
        (UNKNOWN, 'Unknown'),
    )

    type = models.CharField(max_length=7, choices=PET_TYPES, default=UNKNOWN)
    name = models.CharField(max_length=6, blank=False)
    age = models.IntegerField(blank=False)
    description = models.TextField(blank=False)
    # image_url = models.URLField(blank=False)
    image = models.ImageField(upload_to='pets', blank=True)

    # def save(self, force_insert=False, force_update=False, using=None,
    #          update_fields=None):
    #     db_pet = Pet.objects.get(pk=self.id)
    #     image_path = join(settings.MEDIA_ROOT, str(db_pet.image))
    #     os.remove(image_path)
    #     return super().save(force_insert=force_insert, force_update=force_update, using=using,
    #                         update_fields=update_fields)

    def __str__(self):
        return f'{self.id}; {self.name}; {self.age}'


class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    # test = models.CharField(max_length=2)


class Comment(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    text = models.TextField(blank=False)
