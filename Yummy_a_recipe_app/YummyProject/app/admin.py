from django.contrib import admin
from .models import Yummy
# Register your models here.


class YummyAdmin(admin.ModelAdmin):
    list_display = ('user', 'text', )


admin.site.register(Yummy , YummyAdmin )

