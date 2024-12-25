import json
from django.http import JsonResponse
from game.models import MouseUser


def save_user_data(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            print(data.items())
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
            # Сохраняем данные или выполняем обработку
            else:
                user = MouseUser.objects.get(user_id=data["user_id"])
            return JsonResponse({"data": data})
        except json.JSONDecodeError:
            return JsonResponse({"status": "error", "message": "Invalid JSON"}, status=400)
    return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)



def save_user_data(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            print(data.items())
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
            else:
                user = MouseUser.objects.get(user_id=data["user_id"])
            # Сохраняем user_id в сессии
            request.session["user_id"] = user.user_id
            return JsonResponse({"data": data})
        except json.JSONDecodeError:
            return JsonResponse({"status": "error", "message": "Invalid JSON"}, status=400)
    return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)