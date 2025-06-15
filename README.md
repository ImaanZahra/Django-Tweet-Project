# 🐦 Django Tweet Project - Chai aur Django ☕️

A modern microblogging web application built with **Django 5.2.1**. This project demonstrates core web development concepts including user authentication, tweet CRUD, file uploads, and a responsive Bootstrap UI.

[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://python.org)
[![Django](https://img.shields.io/badge/Django-5.2.1-green.svg)](https://djangoproject.com)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.x-purple.svg)](https://getbootstrap.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 🌟 Features

### ✅ Core Functionality
- 🔐 **Authentication**
  - User signup, login, logout
  - CSRF protection for forms

- 🐤 **Tweet Features**
  - Create, update, delete tweets
  - Image upload with each tweet

- 🎨 **Responsive UI**
  - Bootstrap 5 dark theme
  - Navigation bar with dynamic links
  - Clean, user-friendly interface

---

## 🛠️ Tech Stack

- **Backend**: Django 5.2.1, Python 3.12
- **Frontend**: HTML, CSS, Bootstrap 5
- **Database**: SQLite (local dev)
- **File Uploads**: Django media handling (Pillow)
- **Deployment**: GitHub

---

## 🚀 Getting Started

### 1. Clone the repository


git clone https://github.com/ImaanZahra/Django-Tweet-Project.git
cd Django-Tweet-Project

### 2. Set up virtual environment

python -m venv venv
venv\Scripts\activate  # Windows
# OR
source venv/bin/activate  # Mac/Linux


### 3. Install Dependencies

pip install -r requirements.txt


### 4. Run Migrations

python manage.py makemigrations
python manage.py migrate

### 5. Start development server

python manage.py runserver



Made with 💻, ☕, and Django by Imaan Zahra
Happy coding! 🚀



