calm_blog

A minimal Django-based blog for a charity foundation with user authentication, news posting, admin panel, and TailwindCSS styling.

Features
	•	📰 Add and manage news articles with title, image, content, and automatic slug
	•	🔒 User authentication (login/logout)
	•	🛠 Admin panel with custom model registration
	•	📦 Media uploads (images)
	•	🧩 TailwindCSS integrated for styling
	•	🖥 Header, footer, and scroll-to-section navigation

Project Structure

calm_blog/
├── calm_blog/          # Main Django project settings and urls
├── news/               # News app (models, views, templates)
├── users/              # Custom user profile (optional)
├── static/             # Static files (CSS, JS)
├── templates/          # Base templates (base.html, etc.)
├── media/              # Uploaded images
├── manage.py
└── README.md

Setup

1. Clone the repository

git clone https://github.com/VikTornado/calm_blog.git
cd calm_blog

2. Create and activate virtual environment

python3 -m venv venv
source venv/bin/activate

3. Install dependencies

pip install -r requirements.txt  # If present, otherwise manually install
pip install django

4. Apply migrations

python manage.py makemigrations
python manage.py migrate

5. Create superuser

python manage.py createsuperuser

6. Run development server

python manage.py runserver

Visit http://127.0.0.1:8000 to view the site.
Visit http://127.0.0.1:8000/admin to access the admin panel.

Todo
	•	Rich text editor for content (e.g. CKEditor)
	•	Pagination for news list
	•	User profile pages
	•	Markdown support
	•	Deployment to production

⸻

Created with ❤️ by VikTornado