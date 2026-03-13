from flask import Flask, render_template, request
import requests

app = Flask(__name__)  

# Function to fetch news from Hacker News API with pagination
def get_news(page=1, limit=5):
    offset = (page - 1) * limit
    url = f'https://hacker-news.firebaseio.com/v0/newstories.json'
    response = requests.get(url)
    news_ids = response.json()
    news = []
    for news_id in news_ids[offset:offset+limit]:  
        news_item = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{news_id}.json').json()
        news.append(news_item)
    return news

# Function to fetch jobs from Hacker News API with pagination
def get_jobs(page=1, limit=5):
    offset = (page - 1) * limit
    url = f'https://hacker-news.firebaseio.com/v0/jobstories.json'
    response = requests.get(url)
    job_ids = response.json()
    jobs = []
    for job_id in job_ids[offset:offset+limit]:
        job_item = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{job_id}.json').json()
        jobs.append(job_item)
    return jobs

@app.route('/')
def index():
    news = get_news()
    return render_template('index.html', news=news)

@app.route('/jobs')
def jobs_page():
    jobs = get_jobs()
    return render_template('index.html', jobs=jobs)

if __name__ == '__main__':
    app.run(debug=True)