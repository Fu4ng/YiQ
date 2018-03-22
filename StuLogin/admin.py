from django.contrib import admin

# Register your models here.
from django.contrib import admin
from StuLogin import models

class LoginAdmin(admin.ModelAdmin):
    list_display = ('name','id','index','type')
    ordering = ('-index',)

admin.site.register(models.User,LoginAdmin)