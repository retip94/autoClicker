from django.contrib import admin
from .models import UrlToVisit


# Register your models here.
class UrlToVisitAdmin(admin.ModelAdmin):
    list_display = ('name','iterationTime','url')


admin.site.register(UrlToVisit, UrlToVisitAdmin)



