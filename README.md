# My Garments Shop – Online Clothing Store (2019)

GitHub: https://github.com/akuriprabh/Django_Project
Live Demo: Coming soon on Render 

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org)
[![Django](https://img.shields.io/badge/Django-5.0-green)](https://www.djangoproject.com)

## Overview
A fully functional e-commerce website for selling shirts and bottom wear — my very first complete full-stack project, built in just 4 weeks during college.

Users can:
- Browse garments with images and details
- Search products instantly
- Register and log in securely
- Add items to the cart and place orders
- Receive automated email confirmation after purchase

Admin can:
- Manage products, stock, and categories via Django admin
- View all customer orders

## Features
- Product catalogue & real-time search
- User registration + secure login/logout
- Shopping cart & checkout system
- Automated order confirmation emails
- Responsive design (mobile + desktop)
- Clean Django admin dashboard

## Tech Stack
-Stack
- Backend: Python + Django
- Database: SQLite (ready for PostgreSQL/MySQL)
- Frontend: HTML5, CSS3, Bootstrap 4
- Email: Django SMTP integration

## Screenshots
<img width="947" height="532" alt="image" src="https://github.com/user-attachments/assets/01b60fd4-dc59-4edd-bcef-5935cb4dacc1" />


## How to Run
```bash
# 1. Clone the repo
git clone https://github.com/akuriprabh/mygarmentsshop.git
cd mygarmentsshop

# 2. Create and activate a virtual environment
python -m venv venv

# Windows:
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python manage.py migrate
python manage.py createsuperuser  # create your admin account
python manage.py runserver
