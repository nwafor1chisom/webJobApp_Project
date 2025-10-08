from django.contrib import admin
from .models import Application

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['user', 'job', 'applied_at']
    search_fields = ['user__username', 'job__title']
