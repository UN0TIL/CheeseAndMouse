from django.core.validators import FileExtensionValidator
from django.db import models
from PIL import Image

# Create your models here.
class ClickCounter(models.Model):
    '''
    Модель самой мыши
    '''
    # created = models.DateTimeField(auto_now_add=True)
    count = models.PositiveIntegerField(default=0)
    factor = models.PositiveIntegerField(default=1)


class Condition(models.Model):
    condition = models.CharField(max_length=100)
    point = models.PositiveIntegerField()
    picture = models.ImageField(upload_to='condition/', default='condition/default.png', blank=True, null=True)

    def save(self, *args, **kwargs):
        # Данный код открывает изображение и проверяет, имеет ли оно размер больше 100x100 пикселей.
        # Если это так, изменит размер изображения и сохранит его по тому же пути, по которому он был изначально сохранен (переопределив исходное большое изображение).
        super().save(*args, **kwargs)

        img = Image.open(self.picture.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.picture.path)



class Player(models.Model):
    pass
