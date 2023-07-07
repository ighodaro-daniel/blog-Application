Project Documentation: Blog Application
Overview
blog App is a web application developed using Django framework that allows users to create and manage newsletters. It provides a user-friendly interface for creating newsletter titles and writing articles associated with each title. Users can view a list of existing newsletters, read articles in detail, and delete newsletters as needed.

Installation
Clone the project repository from GitHub: git clone https://github.com/your-username/NewsletterApp.git
Navigate to the project directory: cd webserver
Create a virtual environment: python -m venv myenv
Activate the virtual environment:
For Windows: myenv\Scripts\activate
For Linux/Mac: source myenv/bin/activate
Run database migrations: python manage.py migrate
Start the development server: python manage.py runserver
Usage
Access the application in a web browser: http://localhost:8000/
Create a new newsletter:
On the homepage, enter a title in the "Title" input field.
Write the article content in the "Article" textarea.
Click the "Submit" button to create the newsletter.
View existing newsletters:
On the homepage, a list of existing newsletters will be displayed.
Click on a newsletter title to view the detailed article.
Delete a newsletter:
On the homepage, click the "delete" button next to a newsletter to delete it.
Logout:
Project Structure
manage.py: Django's command-line utility for administrative tasks.
webserver/: The main project directory.
settings.py: Configuration settings for the project.
urls.py: URL configuration for the project.
wsgi.py: WSGI application entry point.
blog/: The newsletter app directory.
models.py: Defines the database models (Question and Choice).
views.py: Contains the views (index, detail, result, deleteText, createText).
urls.py: URL configuration for the app.
templates/: HTML templates for the app.
static/: Static files (CSS, JS) for the app.
venv/: The virtual environment directory.

Django (version 4.2)
...
Contributing

