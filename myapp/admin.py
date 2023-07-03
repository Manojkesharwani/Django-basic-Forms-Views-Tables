from django.contrib import admin
from .models import project

class data(admin.ModelAdmin):
    class Meta:
        model =project
        list_display='__all__'




admin.site.register(project,data)
# Register your models here