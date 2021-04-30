from django.contrib import admin
from .models import Allbum


# Register your models here.
class AllbumAdmin(admin.ModelAdmin):
    list_display = [
        'description',
        'tittle',
        'thumbnail',
        'creation'
    ]


admin.site.register(Allbum, AllbumAdmin)
