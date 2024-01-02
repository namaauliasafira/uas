from django.contrib import admin
from django.urls import include, path
from members.views import *

urlpatterns = [
    path('', index, name='index'),
    path('home', home, name='home'),
    # path('comen', comen, name='comen'),
    # path('contact', contact, name='contact'),
    path('admin/', admin.site.urls),
]