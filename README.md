# HIM - Men’s Clothing Ecommerce Application

**HIM** is a Django-based ecommerce application for a men’s clothing brand.

---

## Tech Stack

- Python
- Django
- Built-in Django admin panel
- Database (default: SQLite, configurable)
- Stripe API for payment processing

---

## Setup & Run Locally

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd ecommerce-app
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure environment variables:**

   Create a `.env` file (or set environment variables) with these keys:

   ```
   STRIPE_SECRET_KEY=your_stripe_secret_key
   STRIPE_PUBLISHABLE_KEY=your_stripe_publishable_key
   DJANGO_SECRET_KEY=your_django_secret_key
   ```

   _Note: Missing these, especially Stripe keys, may cause payment features to fail._

4. **Run the development server:**
   ```bash
   python manage.py runserver
   ```
5. **Open your browser at:**  
   [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## Live Demo

Try the deployed app here:  
[https://django-ecommerce-axnp.onrender.com/](https://django-ecommerce-axnp.onrender.com/)
