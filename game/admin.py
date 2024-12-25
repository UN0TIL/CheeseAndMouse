from django.contrib import admin
from .models import Tasks, MouseUser

# Register your models here.


@admin.register(MouseUser)
class MouseUserAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "user_id",
        "count",
        "factor",
    )
    search_fields = (
        "username",
        "user_id",
        "count",
        "factor",
    )



@admin.register(Tasks)
class ConditionAdmin(admin.ModelAdmin):
    list_display = ("condition", "point", "picture")
    search_fields = ("condition", "point", "picture")

    def picture(self, obj):
        return f'<img src="{obj.picture.url}" width="100" height="100">'
