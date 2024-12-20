from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(ClickCounter)
class ClickCounterAdmin(admin.ModelAdmin):
    list_display = ('clicks', 'factor',)
    search_fields = ('clicks', 'factor',)

    def clicks(self, obj):
        return obj.clicks

@admin.register(Condition)
class ConditionAdmin(admin.ModelAdmin):
    list_display = ('condition', 'point', 'picture')
    search_fields = ('condition', 'point', 'picture')

    def picture(self, obj):
        return f'<img src="{obj.picture.url}" width="100" height="100">'