from django.db import models

# Create your models here.
class ClickCounter(models.Model):
    '''
    Модель самой мыши
    '''
    # created = models.DateTimeField(auto_now_add=True)
    count = models.PositiveIntegerField(default=0)
    multiplier = models.PositiveIntegerField(default=1)


class Player(models.Model):
    pass
