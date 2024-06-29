# Calorie Counter

A Django-based web application to track daily calorie consumption.

## Features

- Add new food items with calorie count
- View a list of added food items
- Remove food items from the list
- Calculate and display total calories consumed for the day
- Reset daily calorie count

## Setup Instructions

### Prerequisites

- Python 3.x
- PostgreSQL

### Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd calorie_counter

2. Create and activate a virtual environment:

python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

3. Install dependencies:

pip install -r requirements.txt

4. Set up the database:
# Update your database settings in calorie_counter/settings.py

5. Apply migrations:
python manage.py makemigrations
python manage.py migrate

6. Create a superuser:
python manage.py createsuperuser

7. Run the server:
python manage.py runserver

Usage
Open your web browser and go to http://127.0.0.1:8000/ to access the application.

Deployment
Instructions for deploying the application to Render:

1. Create a Render account and set up a new web service.
2. Connect your GitHub repository and follow the deployment instructions.
3. Add environment variables for DATABASE_URL, SECRET_KEY, etc.
4. Deploy the application.