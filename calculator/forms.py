from django import forms
from .models import CalorieCalculation


class CalorieCalculatorForm(forms.ModelForm):
    class Meta:
        model = CalorieCalculation
        fields = ['age', 'gender', 'weight', 'height', 'activity_level', 'goal']
        widgets = {
            'age': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your age',
                'min': '10',
                'max': '120'
            }),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter weight in kg',
                'step': '0.1',
                'min': '20',
                'max': '500'
            }),
            'height': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter height in cm',
                'step': '0.1',
                'min': '100',
                'max': '250'
            }),
            'activity_level': forms.Select(attrs={'class': 'form-control'}),
            'goal': forms.Select(attrs={'class': 'form-control'}),
        }
        
        labels = {
            'age': 'Age (years)',
            'gender': 'Gender',
            'weight': 'Weight (kg)',
            'height': 'Height (cm)',
            'activity_level': 'Activity Level',
            'goal': 'Goal',
        }