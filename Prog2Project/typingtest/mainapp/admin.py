from django.contrib import admin

from .models import Mainapp

@admin.register(Mainapp)
class MainappAdmin(admin.ModelAdmin):

    list_display = ["content"]

    class Meta:
        model=Mainapp
