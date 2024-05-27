from django.contrib import admin
from .models import UserIntergrationApp, Payment,Plan

# Register your models here.

admin.site.register(UserIntergrationApp)
admin.site.register(Payment)
admin.site.register(Plan)   
# admin.site.register(Subscription)   
