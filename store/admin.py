from django.contrib import admin
from .models import Product, Rubric


class PrAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'content', 'price', 'number', 'rubric')
    list_display_links = ('name',)
    search_fields = ('name', 'content')


admin.site.register(Rubric)
admin.site.register(Product, PrAdmin)
