# KanDO: A to-do Kanban board

This project is a full-stack Kanban board designed to help users plan out their day. It utilizes a SQL-Alchemy backend to store user credentials and notes. The frontend was made with vanila HTML/CSS/JS, and Flask for the backend.

## Site demo

https://github.com/user-attachments/assets/bacc159a-8474-4369-991d-dd0ffbd8a9ca


## Features
- **SQL-Alchemy** database: Stores details including the login credentials, new users, and notes specific to the current user.
- **Flask** backend: Utilized different routes for GET and POST requests, allowing user authentication and database integration.
- **HTML/CSS/JS** frontend: A user-friendly interface of a standard Kanban board allowing users to drag-and-drop their newly created notes. Used vanilla JS for fetch API requests to Flask backend

## Prerequisites
Perform the following installation in your editor
- `pip install flask`
- `pip install Flask-SQLAlchemy`
- `pip install flask-login`
- `pip install flask-wtf`

## Usage
Run the following command in your editor
`py kanban.py`

Thank you for reading!
