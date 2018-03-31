from django.contrib import admin

# Register your models here.
from django.contrib import admin
from StuLogin import models

class UserAdmin(admin.ModelAdmin):
    list_display = ('name','id','index','type')
    ordering = ('-index',)

class FacilityAdmin(admin.ModelAdmin):
    list_display = ('fid','index','type','status')
    ordering = ('-index',)

admin.site.register(models.User,UserAdmin)
admin.site.register(models.Facility,FacilityAdmin)