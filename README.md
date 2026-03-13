# Developers News App

A Flask web application that fetches and displays the latest news and jobs from Hacker News API.

## Features
- Display latest news with titles and links.
- Display latest jobs with titles and links.
- Pagination support.
- Simple and responsive layout using Bootstrap.

## Project Structure
DEVNEWSAPP/
├─ app.py # Main Flask application
├─ templates/ # HTML templates
│ └─ index.html
├─ static/ # Optional CSS/JS
├─ .venv/ # Python virtual environment (ignored in Git)
├─ test_app.py # Unit tests
└─ README.md # Project description

## Requirements
- Python 3.9+
- Flask
- requests

Install dependencies:

```bash
pip install -r requirements.txt

1.Run the Application
Activate the virtual environment:
& .\.venv\Scripts\Activate.ps1

2.Run the Flask app:
python app.py

3.Open your browser at:
http://127.0.0.1:5000/

Testing
Run unit tests:
python -m unittest test_app.py

Usage
Go to / to see the latest news.
Go to /jobs to see the latest jobs.
Use pagination links at the bottom of the page to navigate between pages.

Notes
.venv is ignored in Git, do not push your virtual environment.
Make sure you have a templates/index.html file for rendering.
You can add CSS/JS files in static/ folder if needed.

License
MIT License

## Live Demo
Click here to run the application:
https://sherice-unvitrified-inhospitably.ngrok-free.dev
