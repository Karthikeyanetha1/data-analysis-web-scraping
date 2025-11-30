# Data Analysis by Web Scraping using Python (Django)

Smart web application that collects data from **e-commerce, job portals, news sites and weather APIs**, stores it, and shows it in a clean UI for **admins** and **users**.

Live demo: **https://web-production-7e32a.up.railway.app/**  

---

## 🧩 Features

### 👤 Admin
- Login to **Django Admin** (`/admin/`)
- Activate / deactivate users
- Upload CSV data
- Manage scraping configurations and datasets

### 🙋 User
- Register / Login
- Web scraping for:
  - Flipkart product search
  - Job search
  - News dashboard (using News API)
  - Weather dashboard (using OpenWeather-style API)
- Simple navigation from **User Dashboard**:
  - `search`, `webscrapping`, `News`, `weather`, `logout`

---

## 🛠 Tech Stack

- **Backend:** Python, Django  
- **Frontend:** HTML, CSS  
- **Data & Scraping:** `requests`, `BeautifulSoup`, `pandas`  
- **Database:** SQLite (`db.sqlite3`)  
- **Deployment:** Railway + Gunicorn  
- **Dev Environment:** Can run in **VS Code / PyCharm / Termux**  

---

## 🚀 How to Run (VS Code / Any IDE)

```bash
# 1. Clone the repo
git clone https://github.com/Karthikeyanetha1/data-analysis-web-scraping.git

cd data-analysis-web-scraping/Code

# 2. Create & activate virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS / Termux
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations
python manage.py migrate

# 5. Create a superuser for Django admin
python manage.py createsuperuser

# 6. Run the development server
python manage.py runserver

Open in browser: http://127.0.0.1:8000/

Home: /

User login: /user/

Admin: /admin/



---

🌐 Deployment (Railway)

The app is deployed on Railway using:

Procfile – Gunicorn command for Django

runtime.txt – Python runtime version

requirements.txt – dependencies


Railway builds the environment, installs packages and runs Gunicorn.

Live URL:
👉 https://web-production-7e32a.up.railway.app/


---

🧱 Project Structure (important folders)

project_root/
│
├── admin1/               # Admin views, models & templates
├── user/                 # User registration, login, search & scraping
├── newsApp/              # News dashboard using News API
├── core/                 # Weather app
│
├── assets/
│   ├── templates/        # All HTML templates
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── adminbase.html
│   │   └── user/
│   └── screenshots/      # Screens used in this README
│
├── webscrapping/         # Django project settings + urls
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── db.sqlite3            # Sample data (users, etc.)
├── manage.py
├── Procfile              # Railway / Gunicorn config
└── requirements.txt


---

🔁 High-Level Flow

User / Admin → Django URL Router (webscrapping/urls.py)
             ↓
      App views (admin1 / user / newsApp / core)
             ↓
       Business logic:
         - Web scraping (requests, BeautifulSoup)
         - Data parsing & storage (pandas, models)
         - External APIs (News, Weather)
             ↓
          Templates (assets/templates)
             ↓
         HTML response to browser


---

📸 Screenshots

All screenshots are stored under assets/screenshots/.

Screen	Image

Home Page	
Admin Login	
User Dashboard	
Web Scraper Landing	
Job Search Page	
News Dashboard	
Weather Finder	



---

👥 Team

This project was developed as a team academic project.

G. Neha – Team Lead, planning & coordination

G. Sai Kiran – Backend & scraping logic

G. Brahmakumar – UI, testing & documentation

Gurram Karthikeya – Django integration, deployment (Railway), GitHub setup



---

📈 Possible Future Enhancements

Add graphs/charts for visual data analysis

Export results to CSV / Excel from UI

Better error handling & logging

Dockerize for easier deployment

Make scraping targets configurable from Admin



---

📩 Contact

Gurram Karthikeya – B.Tech CSE (AI & ML)
📍 Telangana, India
📧 karthikeyanetha7@gmail.com
