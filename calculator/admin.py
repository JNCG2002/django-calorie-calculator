from django.contrib import admin
from .models import CalorieCalculation


@admin.register(CalorieCalculation)
class CalorieCalculationAdmin(admin.ModelAdmin):
    list_display = ['id', 'gender', 'age', 'weight', 'height', 'goal', 'recommended_calories', 'created_at']
    list_filter = ['gender', 'goal', 'activity_level', 'created_at']
    search_fields = ['age', 'weight', 'height']
    readonly_fields = ['bmr', 'tdee', 'recommended_calories', 'created_at']
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('age', 'gender', 'weight', 'height')
        }),
        ('Activity & Goals', {
            'fields': ('activity_level', 'goal')
        }),
        ('Calculations', {
            'fields': ('bmr', 'tdee', 'recommended_calories'),
            'classes': ('collapse',)
        }),
        ('System Information', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )