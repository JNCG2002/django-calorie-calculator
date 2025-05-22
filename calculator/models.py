from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class CalorieCalculation(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    
    ACTIVITY_CHOICES = [
        (1.2, 'Sedentary (little or no exercise)'),
        (1.375, 'Lightly active (light exercise 1-3 days/week)'),
        (1.55, 'Moderately active (moderate exercise 3-5 days/week)'),
        (1.725, 'Very active (hard exercise 6-7 days/week)'),
        (1.9, 'Super active (very hard exercise, physical job)'),
    ]
    
    GOAL_CHOICES = [
        ('maintain', 'Maintain Weight'),
        ('lose', 'Lose Weight (0.5 kg/week)'),
        ('gain', 'Gain Weight (0.5 kg/week)'),
    ]
    
    age = models.IntegerField(validators=[MinValueValidator(10), MaxValueValidator(120)])
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    weight = models.FloatField(validators=[MinValueValidator(20), MaxValueValidator(500)])
    height = models.FloatField(validators=[MinValueValidator(100), MaxValueValidator(250)])
    activity_level = models.FloatField(choices=ACTIVITY_CHOICES)
    goal = models.CharField(max_length=10, choices=GOAL_CHOICES)
    
    bmr = models.FloatField()
    tdee = models.FloatField()
    recommended_calories = models.FloatField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def calculate_bmr(self):
        """Calculate BMR using Mifflin-St Jeor Equation"""
        if self.gender == 'M':
            s = 5
        else:
            s = -161
        
        bmr = 10 * self.weight + 6.25 * self.height - 5 * self.age + s
        return round(bmr, 2)
    
    def calculate_tdee(self):
        """Calculate Total Daily Energy Expenditure"""
        return round(self.bmr * self.activity_level, 2)
    
    def calculate_recommended_calories(self):
        """Calculate recommended calories based on goal"""
        if self.goal == 'maintain':
            return self.tdee
        elif self.goal == 'lose':
            # 0.5 kg/week = 3500 calories/week = 500 calories/day deficit
            return round(self.tdee - 500, 2)
        elif self.goal == 'gain':
            # 0.5 kg/week = 3500 calories/week = 500 calories/day surplus
            return round(self.tdee + 500, 2)
    
    def save(self, *args, **kwargs):
        self.bmr = self.calculate_bmr()
        self.tdee = self.calculate_tdee()
        self.recommended_calories = self.calculate_recommended_calories()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Calculation for {self.get_gender_display()} - {self.created_at.strftime('%Y-%m-%d')}"
