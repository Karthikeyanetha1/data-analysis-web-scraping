📊 Data Analysis & Web Scraping using Python (Django Project)

🚀 Live Demo:
👉 https://web-production-7e32a.up.railway.app/

A full-stack Django-based Web Scraping & Data Analysis Platform built using Python, Django, BeautifulSoup, and Pandas.
Users can scrape real-time job listings, Flipkart product data, weather updates, and news.
The project includes complete User and Admin dashboards.


---

✨ Features

👤 User Features

User Registration & Login

Job Search Scraper

Flipkart Product Scraper

Weather Data Scraper

News Headlines Scraper

User Dashboard

Logout


🛠 Admin Features

Admin Login

Manage Users (Activate/Deactivate)

Upload CSV Files

View Registered Users

Admin Dashboard


🌐 Scraping Tools

BeautifulSoup

Requests

Pandas

NewsAPI



---

🧰 Tech Stack

Layer	Technology

Backend	Python 3, Django 2.2
Frontend	HTML, CSS, Bootstrap
Web Scraping	BeautifulSoup, Requests, Pandas
Database	SQLite
Deployment	Railway + Gunicorn
IDE Used	Visual Studio Code
Version Control	Git & GitHub



---

🖥️ Development Setup (Using VS Code)

✔️ 1. Clone the repository

git clone https://github.com/karthikeyanetha1/data-analysis-web-scraping.git
cd data-analysis-web-scraping

✔️ 2. Open project in VS Code

code .

✔️ 3. Create virtual environment

python -m venv venv

✔️ 4. Activate virtual environment

Windows:

venv\Scripts\activate

Mac/Linux:

source venv/bin/activate

✔️ 5. Install dependencies

pip install -r requirements.txt

✔️ 6. Apply migrations

python manage.py migrate

✔️ 7. Run the server

python manage.py runserver


---

🌍 Deployment (Railway)

The project is deployed using:

Procfile

runtime.txt

Gunicorn

Railway build environment


Railway handles hosting + server management automatically.


---

📂 Project Structure

project/
│── admin1/                  # Admin logic
│── user/                    # User logic
│── newsApp/                 # News scraper
│── core/                    # Job, Flipkart, weather scrapers
│── webscrapping/            # Django settings + URLs
│── assets/templates/        # All HTML templates
│── static/                  # CSS / JS files
│── manage.py
│── requirements.txt
│── Procfile
│── runtime.txt


---

👤 Author

Gurram Karthikeya
B.Tech – CSE (AI & ML)
📍 Telangana, India
📧 karthikeyanetha7@gmail.com
