from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Tasks, MouseUser


@receiver(post_save, sender=Tasks)
def distribute_task_to_all_users(sender, instance, created, **kwargs):
    if created:  # Действуем только при создании нового задания
        users = MouseUser.objects.all()  # Получаем всех пользователей

        # Создаём задания для всех пользователей
        tasks_to_create = []

        for user in users:
            tasks_to_create.append(Tasks(
                user = user,
                condition=instance.condition, # Используем related_name 'tasks'
                point=instance.point,
                times=instance.times,
                url=instance.url,
                picture=instance.picture  # Указываем путь к картинке
            ))

        # Массовое создание задач для всех пользователей
        Tasks.objects.bulk_create(tasks_to_create)

        # Удаляем первоначально созданный объект
        instance.delete()