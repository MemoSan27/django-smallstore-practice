from django.contrib import admin
from .models import Brand, Comment, Product

admin.site.register(Product);
admin.site.register(Brand);
admin.site.register(Comment);
