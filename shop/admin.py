from django.contrib import admin
from shop.models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

    
admin.site.register(Category, CategoryAdmin)
