from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from .models import Tasks, MouseUser
import json


# !!!!!!!!!!!!!!
# Аунтификация
# !!!!!!!!!!!!!!

def save_user_data(request):

    if request.method == "POST":
        try:
            data = json.loads(request.body)
            print(data)
            if data["user_id"] not in MouseUser.objects.values_list(
                "user_id", flat=True
            ):
                user = MouseUser(
                    first_name=data["first_name"],
                    username=data["username"],
                    user_id=data["user_id"],
                    language_code=data["language_code"],
                    is_premium=data["is_premium"],
                )
                request.session["user_id"] = user.user_id
                user.save()
            else:
                user = MouseUser.objects.get(user_id=data["user_id"])

                request.session["user_id"] = user.user_id

            return JsonResponse({"data": data})
        except json.JSONDecodeError:
            return JsonResponse({"status": "error", "message": "Invalid JSON"}, status=400)

    elif request.method == "GET":
        user_id = request.session.get("user_id")

        if not user_id:
            return JsonResponse({"error": "User ID not found in session!!!!"}, status=400)

        user, created = MouseUser.objects.get_or_create(user_id=user_id)

        return render(request, "game/main_page.html", {"user": user})

    return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)


# !!!!!!!!!!!!!!
# Нижняя панель
# !!!!!!!!!!!!!!

def main_page_view(request):

    user_id = request.session.get("user_id")

    if not user_id:
        return HttpResponseRedirect('/game/save_user_data/')

    user, created = MouseUser.objects.get_or_create(user_id=user_id)

    return render(request, "game/main_page.html", {"user": user})


def tasks_view(request):

    user_id = request.session.get("user_id")

    if not user_id:
        return JsonResponse({"error": "User ID not found in session"}, status=400)

    tasks = Tasks.objects.filter(user__user_id=user_id)

    user, created = MouseUser.objects.get_or_create(user_id=user_id)

    return render(request, "game/tasks.html", {"tasks": tasks, "user": user})


def friends_view(request):

    user_id = request.session.get("user_id")

    if not user_id:
        return JsonResponse({"error": "User ID not found in session"}, status=400)

    user, created = MouseUser.objects.get_or_create(user_id=user_id)

    return render(request, "game/friends.html", {"user": user})


# !!!!!!!!!!!!!!
# Механики игры
# !!!!!!!!!!!!!!

def increment_count(request):

    user_id = request.session.get("user_id")

    if not user_id:
        return JsonResponse({"error": "User ID not found in session"}, status=400)

    if request.method == "POST":
        try:
            user, created = MouseUser.objects.get_or_create(user_id=user_id)

            user.count += 1 * user.factor
            user.save()

            # if user.count >= 1000:
            #     print(user.count)
            #     return HttpResponseRedirect('/winner/')

            return JsonResponse({"count": user.count})
        except MouseUser.DoesNotExist:
            return JsonResponse({"error": "User not found"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=405)



def mission_view(request):
    user_id = request.session.get("user_id")

    # Проверяем, есть ли user_id в сессии
    if not user_id:
        return JsonResponse({"error": "User ID not found in session"}, status=400)

    if request.method == "POST":
        try:
            # Загружаем данные из запроса
            data = json.loads(request.body)
            print('Incoming Data:', data)  # Для проверки входящих данных

            # Проверяем, что поле "point" существует и содержит массив
            if "point" not in data or not isinstance(data["point"], list) or not data["point"]:
                return JsonResponse({"error": "Invalid or missing 'point' field"}, status=400)


            if "id" not in data or not isinstance(data["id"], list) or not data["id"]:
                return JsonResponse({"error": "Invalid or missing 'point' field"}, status=400)

            # Проверяем, что каждый элемент в поле "point" можно преобразовать в число
            points = list(map(int, data["point"]))
            id = list(map(int, data['id']))# Преобразуем список в числа
            print('Parsed Points:', points)

            # Получаем пользователя
            user = MouseUser.objects.get(user_id=user_id)

            # Получаем задачу с указанным "point"
            task = Tasks.objects.filter(user__user_id=user_id).get(id=id[0])

            # Обновляем или удаляем задачу
            if task.times - 1 <= 0:
                task.delete()  # Если больше попыток не осталось, удаляем
            else:
                task.times -= 1
                task.save()  # Уменьшаем оставшиеся попытки

            # Обновляем счётчик пользователя
            user.count += sum(points)
            user.save()

            if user.count >= 1000:
                return HttpResponseRedirect('/winner/')

            return JsonResponse({
                "count": user.count,
                "message": "Task processed successfully."
            })

        # Обрабатываем случай с отсутствием задачи
        except Tasks.DoesNotExist:
            return JsonResponse({"error": "Task with the specified point does not exist."}, status=404)

        # Обрабатываем ошибки JSON-данных
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)

        # Обрабатываем все другие возможные ошибки
        except Exception as e:
            return JsonResponse({"error": f"Unexpected error: {str(e)}"}, status=500)

    # Если метод не POST
    return JsonResponse({"error": "Invalid request method"}, status=405)



def upper(request):

    user_id = request.session.get("user_id")
    if not user_id:
        return JsonResponse({"error": "User ID not found in session"}, status=400)

    if request.method == "POST":
        user, created = MouseUser.objects.get_or_create(user_id=user_id)

        if user.count > 10:

            user.factor += 1
            user.count -= 10

            user.save()

            return JsonResponse({"multiplier": user.factor, "count": user.count})
    return JsonResponse({"error": "Invalid request"}, status=400)


def autoclick(request):

    user_id = request.session.get("user_id")

    if not user_id:
        return JsonResponse({"error": "User ID not found in session"}, status=400)

    if request.method == "POST":
        user, created = MouseUser.objects.get_or_create(user_id=user_id)

        user.count += 1  # Увеличиваем значение счётчика на 1
        user.save()
        return JsonResponse({"count": user.count})
    return JsonResponse({"error": "Invalid request"}, status=400)