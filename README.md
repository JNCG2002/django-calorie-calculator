# Django Calorie Calculator

A web-based calorie calculator built with Django, based on the Mifflin-St Jeor Equation and statistical research in nutrition science.

## Features

- **Scientific Accuracy**: Based on the Mifflin-St Jeor Equation, a validated statistical model
- **Comprehensive Calculation**: Calculates BMR, TDEE, and personalized calorie recommendations
- **Multiple Goals**: Support for weight maintenance, loss, and gain
- **Responsive Design**: Mobile-friendly interface using Bootstrap
- **Educational Content**: Detailed explanations of the statistical models used

## Technologies Used

- Django 4.2.7
- Bootstrap 5.1.3
- SQLite Database
- HTML5/CSS3/JavaScript

## Installation and Setup

### Prerequisites
- Python 3.8 or higher
- Git

### Local Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/django-calorie-calculator.git
   cd django-calorie-calculator
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # source venv/bin/activate  # On Mac/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Open browser and go to `http://127.0.0.1:8000/`

## Deployment

### GitHub Pages (Static Hosting)
This Django app requires a server to run. For static hosting, consider converting to a static site or use services like Heroku.

### Heroku Deployment
1. Create a Heroku account
2. Install Heroku CLI
3. Create new Heroku app
4. Deploy using Git

```bash
heroku create your-app-name
git push heroku main
heroku run python manage.py migrate
```

## Usage

1. **Enter Personal Information**: Age, gender, weight, and height
2. **Select Activity Level**: Choose from sedentary to super active
3. **Choose Goal**: Maintain, lose, or gain weight
4. **Get Results**: View BMR, TDEE, and recommended daily calories
5. **Learn More**: Read about the statistical models used

## Statistical Model

The calculator uses the **Mifflin-St Jeor Equation**:

```
BMR = 10 × weight(kg) + 6.25 × height(cm) - 5 × age(years) + s
```

Where:
- s = +5 for males
- s = -161 for females

**TDEE Calculation**:
```
TDEE = BMR × Activity Factor
```

Activity factors:
- Sedentary: 1.2
- Lightly Active: 1.375
- Moderately Active: 1.55
- Very Active: 1.725
- Super Active: 1.9

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License.

## References

- Mifflin, M. D., et al. (1990). A new predictive equation for resting energy expenditure in healthy individuals. The American Journal of Clinical Nutrition, 51(2), 241-247.
- Frankenfield, D., et al. (2005). Comparison of predictive equations for resting metabolic rate in healthy nonobese and obese adults: a systematic review. Journal of the American Dietetic Association, 105(5), 775-789.