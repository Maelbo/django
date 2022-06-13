from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Machine , Personnel

admin.site.register(Machine)
admin.site.register(Personnel)
