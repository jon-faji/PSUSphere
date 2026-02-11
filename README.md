# PSUSphere Project

A Django-based web application for managing college, program, student, and organization information.

## Login Credentials
- **Username:** admin
- **Password:** admin123

## Setup Instructions

1. Clone the repository
```bash
git clone [repository-url]
cd psuphere
```
2. Create and activate virtual environment
```bash
python -m venv myenv
# For Windows
myenv\Scripts\activate

3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Setup the database
```bash

python manage.py migrate
```
5. Create superuser (if not already created)
```bash
python manage.py createsuperuser
```
6. Run the development server
```bash
python manage.py runserver
```
Access the application at: 

## Features
- College Management
- Program Management
- Student Information System
- Organization Management
- Organization Membership Tracking
- User Authentication
- Responsive Dashboard

## Project Structure
- `projectsite/` - Main project directory
  - `templates/` - HTML templates
  - `static/` - Static files (CSS, JavaScript, Images)
  - `projectsite/` - Project settings and configuration
