from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CalorieCalculatorForm
from .models import CalorieCalculation


def home(request):
    """Home page with calculator form"""
    if request.method == 'POST':
        form = CalorieCalculatorForm(request.POST)
        if form.is_valid():
            calculation = form.save()
            return redirect('result', calculation_id=calculation.id)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CalorieCalculatorForm()
    
    return render(request, 'calculator/home.html', {'form': form})


def result(request, calculation_id):
    """Display calculation results"""
    try:
        calculation = CalorieCalculation.objects.get(id=calculation_id)
        context = {
            'calculation': calculation,
            'bmr_explanation': get_bmr_explanation(),
            'activity_explanation': get_activity_explanation(),
        }
        return render(request, 'calculator/result.html', context)
    except CalorieCalculation.DoesNotExist:
        messages.error(request, 'Calculation not found.')
        return redirect('home')


def about(request):
    """About page with research information"""
    return render(request, 'calculator/about.html')


def get_bmr_explanation():
    """Return BMR explanation text"""
    return """
    Basal Metabolic Rate (BMR) is the number of calories your body needs to maintain 
    basic physiological functions like breathing, circulation, and cell production while at rest. 
    This calculation uses the Mifflin-St Jeor Equation, which is based on statistical 
    regression analysis of metabolic data from healthy adults.
    """


def get_activity_explanation():
    """Return activity level explanation"""
    return """
    Total Daily Energy Expenditure (TDEE) is calculated by multiplying your BMR by 
    an activity factor. These multipliers are derived from empirical studies and 
    represent different levels of physical activity throughout the day.
    """