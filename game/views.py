import json

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import ClickCounter

# Нижняя панель

def main_page_view(request):
    counter, created = ClickCounter.objects.get_or_create(id=1)
    return render(request, 'game/main_page.html', {'counter': counter.count})

def tasks_view(request):
    context = {
        'tasks': [
            {'name': 'Subscribe to Telegram', 'reward': 200},
            {'name': 'Watch the video', 'reward': 250},
            {'name': 'Like the post', 'reward': 100},
            {'name': 'Watch an ad', 'reward': 300},
        ]
    }
    return render(request, 'game/tasks.html', context)  # Правильный способ


def friends_view(request):
    pass
from django.shortcuts import render


# Механики игры

def increment_count(request):
    if request.method == 'POST':
        counter, created = ClickCounter.objects.get_or_create(id=1)
        counter.count += (1 * counter.multiplier)
        counter.save()
        return JsonResponse({'count': counter.count})
    return JsonResponse({'error': 'Invalid request'}, status=400)

def mission_view(request):
    if request.method == 'POST':
        counter, created = ClickCounter.objects.get_or_create(id=1)
        data = json.loads(request.body)
        numbers = sum(data['numbers'])

        counter.count += numbers
        counter.save()

        return JsonResponse({'count': counter.count})
    return JsonResponse({'error': 'Invalid request'}, status=400)

def upper(request):
    if request.method == 'POST':
        counter, created = ClickCounter.objects.get_or_create(id=1)
        if counter.count > 10:
            counter.multiplier += 1
            counter.count -= 10
            counter.save()
            return JsonResponse({'multiplier': counter.multiplier, 'count': counter.count})
    return JsonResponse({'error': 'Invalid request'}, status=400)

def autoclick(request):
    if request.method == 'POST':
        counter, created = ClickCounter.objects.get_or_create(id=1)
        counter.count += 1  # Увеличиваем значение счётчика на 1
        counter.save()
        return JsonResponse({'count': counter.count})
    return JsonResponse({'error': 'Invalid request'}, status=400)
    # if request.method == 'POST':
    #     counter, created = ClickCounter.objects.get_or_create(id=1)
    #     while counter.count < 30:
    #         counter.count += 1
    #         sleep(1)
    #         counter.save()
    #         return JsonResponse({'count': counter.count})
    # return JsonResponse({'error': 'Invalid request'}, status=400)


