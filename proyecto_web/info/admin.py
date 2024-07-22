from django.contrib import admin
from .models import Informacion

# Register your models here.
class InformacionAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    
admin.site.register(Informacion, InformacionAdmin)