from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    search_fields = ('email','username',)
    list_filter = ('id', 'username','email',)
    list_display = ('id', 'username','email','created_at',)


admin.site.register(User,UserAdmin)