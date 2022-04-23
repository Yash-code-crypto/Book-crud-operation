from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin






admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(Language)

