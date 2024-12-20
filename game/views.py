import inspect

from django.shortcuts import render
from django.http import JsonResponse
from .models import ClickCounter, Condition
import json
# !!!!!!!!!!!!!!
# Нижняя панель
# !!!!!!!!!!!!!!

def main_page_view(request):
    counter, created = ClickCounter.objects.get_or_create(id=1)
    return render(request, 'game/main_page.html', {'counter': counter.count})

def tasks_view(request):
    tasks = Condition.objects.all()
    # for task in tasks:
        # print(*task.__dict__.items(), sep='\n')
    return render(request, 'game/tasks.html', {'tasks': tasks})  # Правильный способ


def friends_view(request):
    pass

# !!!!!!!!!!!!!!
# Механики игры
# !!!!!!!!!!!!!!


def increment_count(request):
    if request.method == 'POST':
        counter, created = ClickCounter.objects.get_or_create(id=1)
        counter.count += (1 * counter.factor)
        counter.save()
        return JsonResponse({'count': counter.count})
    return JsonResponse({'error': 'Invalid request'}, status=400)

def mission_view(request):
    if request.method == 'POST':
        counter, created = ClickCounter.objects.get_or_create(id=1)
        try:
            data = json.loads(request.body)

            if 'points' not in data or not isinstance(data['points'], list):
                return JsonResponse({'error': 'Invalid request'}, status=400)
            points = sum(data['points'])
            counter.count += points
            counter.save()

            return JsonResponse({'count': counter.count})
        except (ValueError, TypeError) as e:
            return JsonResponse({'error': f'Invalid JSON, Вот проблема: {e}'}, status=400)
    return JsonResponse({'error': 'Invalid request'}, status=400)

def upper(request):
    if request.method == 'POST':
        counter, created = ClickCounter.objects.get_or_create(id=1)
        if counter.count > 10:
            counter.factor += 1
            counter.count -= 10
            counter.save()
            return JsonResponse({'multiplier': counter.factor, 'count': counter.count})
    return JsonResponse({'error': 'Invalid request'}, status=400)

def autoclick(request):
    if request.method == 'POST':
        counter, created = ClickCounter.objects.get_or_create(id=1)
        counter.count += 1  # Увеличиваем значение счётчика на 1
        counter.save()
        return JsonResponse({'count': counter.count})
    return JsonResponse({'error': 'Invalid request'}, status=400)



