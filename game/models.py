from django.core.validators import MinValueValidator
from django.db import models
from PIL import Image


class MouseUser(models.Model):
    """
    Модель для представления пользователя.
    Атрибуты:
        - first_name: Имя пользователя (строка до 100 символов).
        - username: Уникальный ник пользователя (строка до 100 символов).
        - user_id: Уникальный идентификатор пользователя (положительное число).
        - count: Количество монет (положительное число, минимальное значение 0).
        - factor: Множитель для игровых механик (положительное число, по умолчанию 1).
        - date_create: Дата и время создания профиля.
        - date_updated: Дата и время последнего обновления профиля.
        - language_code: Код языка пользователя (строка до 8 символов, по умолчанию "ru").
        - is_premium: Флаг, указывающий, является ли пользователь премиум.
        - is_staff: Флаг, указывающий, является ли пользователь администратором.
    """
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
        """Возвращает строковое представление пользователя (его ник)."""
        return self.username


class Tasks(models.Model):
    """
    Модель для представления задания.
    Атрибуты:
        - user: Ссылка на пользователя, связанного с заданием (MouseUser).
        - condition: Описание задания (строка до 100 символов).
        - point: Количество очков, начисляемых за выполнение задания (положительное число).
        - times: Количество раз, которое задание можно выполнить (положительное число, по умолчанию 1).
        - url: Ссылка, связанная с заданием (URL-адрес, необязательное поле).
        - picture: Изображение задания (загружается в папку "condition/", по умолчанию "condition/default.png").
    """
    user = models.ForeignKey(MouseUser, on_delete=models.CASCADE, related_name="tasks", blank=True, null=True)
    condition = models.CharField(max_length=100, verbose_name='Описание задания')
    point = models.PositiveIntegerField(verbose_name="Очки")
    times = models.PositiveIntegerField(default=1, verbose_name="Попытки")
    url = models.URLField(default="", blank=True, verbose_name="Ссылка")
    picture = models.ImageField(
        upload_to="condition/", default="condition/default.png", blank=True, verbose_name="Изображение")

    class Meta:
        ordering = ['condition', 'point', 'picture']
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

    def __str__(self):
        """Возвращает строковое представление задания (его описание)."""
        return self.condition

    def save(self, *args, **kwargs):
        """
        Переопределённый метод сохранения модели.
        Уменьшает размер изображения до 100x100 пикселей, если исходное изображение превышает эти размеры.
        """
        super().save(*args, **kwargs)

        img = Image.open(self.picture.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.picture.path)

