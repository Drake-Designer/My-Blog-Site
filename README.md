# 📝 My Blog Site

🌍 **Live Demo:** [my-blog-site on Heroku](https://my-blog-site-a847981c248e.herokuapp.com/)

I built **My Blog Site** with **Django** so I can share what I learn about code, music, and day-to-day life. Readers can browse posts, save favourites for later, and leave quick comments without creating an account. I keep the setup lean so deploying to **Heroku** with **WhiteNoise** and **Cloudinary** stays easy.

---

## 📌 Project Overview

The application includes:

- **Content Publishing**  
   I draft posts in Django admin with authors, tags, slugs, and Cloudinary images.

- **Comments**  
   Visitors fill a tiny form and their message appears immediately on the post page.

- **Read Later**  
   Readers drop posts into a session-based list and clear it whenever they want.

- **Responsive Layout**  
   Templates stay tidy on phones and desktops thanks to reusable includes and CSS.

- **Cloud-Ready Media**  
   Post images live in Cloudinary so deployment stays simple.

- **Admin Shortcuts**  
   Search, filters, and auto-generated slugs make my publishing workflow fast.

---

## 🛠️ Technologies Used

- **Python 3.13**  
- **Django 5.2** (main framework)  
- **SQLite** locally, **PostgreSQL** when `DATABASE_URL` is set  
- **Cloudinary** + `django-cloudinary-storage` (image hosting)  
- **WhiteNoise** (static file handling on Heroku)  
- **Gunicorn** (production server)  
- **python-dotenv** (local environment variables)

---

## 📚 What I Learned

- Designing Django models so authors, tags, posts, and comments work well together.  
- Serving static files with **WhiteNoise** while keeping uploaded images in **Cloudinary**.  
- Mixing class-based list views with custom logic for detail pages and session storage.  
- Validating comment input through Django forms to keep the data clean.  
- Loading fixtures to share sample content quickly.  
- Preparing a project for **Heroku** with environment variables and a `Procfile`.

---

## 📊 Example Features

### 🏠 Home Page

- Shows a welcome message and my three newest posts.  
- Highlights each post with a card and tag list.

### 📚 All Posts

- Lists every post with consistent styling.  
- Makes it easy to jump to any article.

### 📝 Post Detail Page

- Displays the full story, tags, and author contact link.  
- Lets readers drop a comment and toggle the read-later option.

### 📥 Read Later Shelf

- Stores saved posts inside the session.  
- Lets readers remove items as soon as they finish.

---

## 🚀 Deployment

The project is ready for **Heroku** or a similar platform.

1. Clone the repo:

   ```powershell
   git clone https://github.com/Drake-Designer/my-blog-site.git
   cd my-blog-site
   ```

2. Create a virtual environment:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. Install dependencies:

   ```powershell
   pip install -r requirements.txt
   ```

4. Add a `.env` file with `SECRET_KEY`, `ALLOWED_HOSTS`, Cloudinary settings, and optional `DATABASE_URL`.  
5. Apply migrations and load sample data if you want demo content:

   ```powershell
   python manage.py migrate
   python manage.py loaddata blog/fixtures/seed_all.json
   ```

6. Run the app locally:

   ```powershell
   python manage.py runserver
   ```

7. Before deploying, run `python manage.py collectstatic`, set `DATABASE_URL`, and use `gunicorn my_blog_site.wsgi` on the host.


## 🤝 Contributing

Issues and pull requests are welcome! Please open an issue describing the change you have in mind. For larger features, consider forking the repo, working on a feature branch, and submitting a PR once tests pass.

---

## 📄 License

This project is released under the MIT License. See `LICENSE` (add one if missing) for details.
