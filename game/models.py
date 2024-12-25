from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator, MinValueValidator
from django.db import models
from PIL import Image


class MouseUser(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Имя пользователя")
    username = models.CharField(
        max_length=100, unique=True, verbose_name="Ник пользователя"
    )
    user_id = models.PositiveBigIntegerField(unique=True, verbose_name="User ID")
    count = models.PositiveIntegerField(
        default=0, verbose_name="Монеты", validators=[MinValueValidator(0)]
    )
    factor = models.PositiveIntegerField(default=1, verbose_name="Множитель")
    date_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    date_updated = models.DateTimeField(auto_now=True, verbose_name="Время обновления")
    language_code = models.CharField(
        max_length=8, default="ru", verbose_name="Код языка"
    )
    is_premium = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    class Meta:
        ordering = ["username"]
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

    def __str__(self):
        return self.username


class Tasks(models.Model):
    condition = models.CharField(max_length=100)
    point = models.PositiveIntegerField()
    picture = models.ImageField(
        upload_to="condition/", default="condition/default.png", blank=True, null=True
    )

    class Meta:
        ordering = ['condition', 'point', 'picture']
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

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
