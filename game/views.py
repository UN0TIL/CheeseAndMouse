from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Tasks, MouseUser
import json


# !!!!!!!!!!!!!!
# Нижняя панель
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
                )
                user.save()
                print('here')
            else:
                user = MouseUser.objects.get(user_id=data["user_id"])
                print('here2')
            # Сохраняем user_id в сессии
            # print(user.__dict__)
            request.session["user_id"] = user.user_id
            return JsonResponse({"data": data})
        except json.JSONDecodeError:
            return JsonResponse({"status": "error", "message": "Invalid JSON"}, status=400)
    return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)


def main_page_view(request):

    user_id = request.session.get("user_id")
    print('!!!!!!!!!!!!!!!!!!')
    print(user_id)

    if not user_id:
        return JsonResponse({"error": "User ID not found in session!!!!"}, status=400)

    user, created = MouseUser.objects.get_or_create(user_id=user_id)

    return render(request, "game/main_page.html", {"user": user})


def tasks_view(request):

    tasks = Tasks.objects.all()

    user_id = request.session.get("user_id")

    if not user_id:
        return JsonResponse({"error": "User ID not found in session"}, status=400)

    user, created = MouseUser.objects.get_or_create(user_id=user_id)

    return render(
        request, "game/tasks.html", {"tasks": tasks, "user": user}
    )  # Правильный способ


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

            return JsonResponse({"count": user.count})
        except MouseUser.DoesNotExist:
            return JsonResponse({"error": "User not found"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=405)


def mission_view(request):

    user_id = request.session.get("user_id")
    if not user_id:
        return JsonResponse({"error": "User ID not found in session"}, status=400)

    if request.method == "POST":
        user, created = MouseUser.objects.get_or_create(user_id=user_id)

        try:
            data = json.loads(request.body)

            if "points" not in data or not isinstance(data["points"], list):
                return JsonResponse({"error": "Invalid request"}, status=400)

            points = sum(data["points"])

            user.count += points
            user.save()

            return JsonResponse({"count": user.count})
        except (ValueError, TypeError) as e:
            return JsonResponse(
                {"error": f"Invalid JSON, Вот проблема: {e}"}, status=400
            )
    return JsonResponse({"error": "Invalid request"}, status=400)


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
