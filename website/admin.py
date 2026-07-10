from django.contrib import admin
from website.models import contact

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ['name', 'Email', 'created_date']
    list_filter = ('Email',)
    search_fields = ('name', 'message')
admin.site.register(contact,ContactAdmin)