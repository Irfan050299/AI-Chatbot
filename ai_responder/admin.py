from django.contrib import admin
from .models import QueryResponse
# Register your models here.

@admin.register(QueryResponse)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','email','question','response']
