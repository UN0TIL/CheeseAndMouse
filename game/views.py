from django.shortcuts import render
from django.http import JsonResponse
from .models import ClickCounter
from time import sleep

def index(request):
    counter, created = ClickCounter.objects.get_or_create(id=1)
    return render(request, 'game/index.html', {'counter': counter.count})

def increment_count(request):
    if request.method == 'POST':
        counter, created = ClickCounter.objects.get_or_create(id=1)
        counter.count += (1 * counter.multiplier)
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