from django.contrib import admin
from.models import User

# Register your models here.

class MemberUser():
    list_display = ("NAMA",)

admin.site.register(User)    
