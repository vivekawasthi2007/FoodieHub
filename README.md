# 🍔 FoodieHub — Online Food Ordering & Delivery Web Application

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Django Version](https://img.shields.io/badge/Django-5.0%20%7C%206.0-green?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-CDN-38B2AC?logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)
[![Database](https://img.shields.io/badge/Database-SQLite-003B57?logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**FoodieHub** is a modern, responsive, full-stack food ordering and delivery web application built with **Python**, **Django**, and **Tailwind CSS**. It provides a seamless food ordering experience — from exploring an extensive multi-category menu and maintaining a personal favorites list, to managing a shopping cart and tracking live delivery countdowns in real-time.

---

## ✨ Features

### 🍔 Menu & Discovery
- **Rich Menu Catalog:** Filter and explore delicious dishes categorized into Starters & Snacks, Main Course, Pizzas & Pastas, Desserts, and Beverages.
- **Instant Search:** Search items in real time by name (`?q=pizza`, `burger`, etc.).
- **Interactive Wishlist:** Like/unlike food items on the fly with animated toggle buttons and a dedicated Favorites dashboard.

### 🛒 Shopping Cart & Checkout
- **Cart Management:** Add food items with automatic quantity updates and real-time total price calculation.
- **One-Click Checkout:** Automatically pulls your saved delivery address from your profile for quick checkout.
- **Clean Confirmation:** Immediate order creation with unique Order ID and instant cart cleanup.

### ⏱️ Live Order Tracking & History
- **Real-Time Countdown Timer:** Dynamic 30-minute delivery countdown calculated via JavaScript from server timestamps.
- **Dynamic Order Statuses:** Visual tracking badges (`Pending` 🟡, `Preparing` 🟠, `Out for Delivery` 🚚, `Delivered` 🟢).
- **Order History:** Complete log of previous orders with timestamps, delivery address, and total amounts.

### 👤 User Authentication & Profiles
- **Authentication:** Secure user registration, login, and logout powered by Django's robust auth framework.
- **Profile Dashboard:** Manage profile details, phone numbers, delivery addresses, and profile pictures.

### ⚡ Pre-Configured Database Seeder
- Includes `seed.py` to instantly populate **100+ realistic menu items** complete with emojis, prices in INR (₹), and descriptions.

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | Python 3.10+, Django (App-based architecture: `accounts`, `menu`, `order`) |
| **Frontend** | HTML5, Tailwind CSS (Utility-first styling via CDN), Vanilla JavaScript |
| **Database** | SQLite (Default, easily configurable for PostgreSQL / MySQL) |
| **Templating** | Django Template Language (DTL) |
| **Admin Panel**| Django Admin (Manage users, categories, menu items, and orders) |

---

## 📂 Project Structure

```text
FoodieHub/
├── foodiehub/                   # Django Project Root
│   ├── accounts/                # User authentication & profile management
│   │   ├── migrations/
│   │   ├── templates/accounts/  # login.html, register.html, profile.html
│   │   ├── models.py            # UserProfile model
│   │   ├── urls.py
│   │   └── views.py
│   ├── menu/                    # Food catalog, categories & wishlist
│   │   ├── migrations/
│   │   ├── templates/menu/      # index.html, wishlist.html
│   │   ├── models.py            # Category, FoodItem, WishlistItem
│   │   ├── urls.py
│   │   └── views.py
│   ├── order/                   # Cart, checkout & live order tracking
│   │   ├── migrations/
│   │   ├── templates/order/     # cart.html, order_status.html, order_history.html
│   │   ├── models.py            # CartItem, OrderMaster (30-min timer logic)
│   │   ├── urls.py
│   │   └── views.py
│   ├── foodiehub/               # Project configuration settings & routing
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── db.sqlite3               # SQLite Database
│   ├── manage.py                # Django CLI entrypoint
│   └── seed.py                  # Database seeder script (100+ food items)
├── .gitignore
├── LICENSE                      # MIT License
└── README.md                    # Project Documentation
```

---

## 🚀 Getting Started

Follow these steps to set up and run FoodieHub locally on your machine:

### 1. Clone the Repository
```bash
git clone https://github.com/vivekawasthi2007/FoodieHub.git
cd FoodieHub/foodiehub
```

### 2. Create and Activate a Virtual Environment

**On Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**On macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Required Dependencies
Install the required Python packages (`Django` and `Pillow` for image handling):
```bash
pip install -r requirements.txt
```
*(Or install directly):*
```bash
pip install django pillow
```

### 4. Apply Database Migrations
Set up all the required database tables:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Seed the Database with Sample Food Items
Populate the database with over 100+ menu items across Starters, Main Course, Pizzas, Desserts, and Drinks:
```bash
python seed.py
```

### 6. Create a Superuser (Admin Access)
```bash
python manage.py createsuperuser
```

### 7. Run the Development Server
```bash
python manage.py runserver
```

Open your browser and visit: **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

---

## 🗺️ Key Application Routes

| Route | View | Description |
|---|---|---|
| `/` | `menu:menu_page` | Home page with search and food catalog |
| `/wishlist/` | `menu:wishlist_page` | User's favorite saved food items |
| `/wishlist/toggle/<id>/` | `menu:toggle_wishlist` | Add / remove item from wishlist |
| `/auth/register/` | `accounts:register_view`| New user sign up |
| `/auth/login/` | `accounts:login_view` | User login |
| `/auth/logout/` | `accounts:logout_view` | User logout |
| `/auth/profile/` | `accounts:profile_view` | Manage contact & delivery address |
| `/auth/my-cart/` | `order:cart_view` | View shopping cart & total price |
| `/auth/add/<id>/` | `order:add_to_cart` | Add item to shopping cart |
| `/auth/checkout` | `order:checkout_view` | Place order with saved address |
| `/auth/status/<id>/` | `order:order_status_view` | Live 30-minute delivery countdown timer |
| `/auth/my-order/` | `order:order_history_view` | Order history & past purchases |
| `/admin/` | Django Admin | Admin dashboard to manage records |

---

## 🛡️ Database Models Overview

- **`Category`**: Food categories (Starters & Snacks, Main Course, Pizzas & Pastas, Desserts, Beverages).
- **`FoodItem`**: Name, category, description, price, and availability flag.
- **`WishlistItem`**: Many-to-one link between User and FoodItem for favorites.
- **`CartItem`**: User cart contents with quantity counter and dynamic total calculation.
- **`OrderMaster`**: Orders with delivery address, status workflow (`Pending`, `Preparing`, `Out for Delivery`, `Delivered`), and automatically calculated 30-minute `estimated_delivery_time`.
- **`UserProfile`**: User profile model extending `auth.User` with phone number, delivery address, and profile picture.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📜 License

Distributed under the **MIT License**. See the [`LICENSE`](LICENSE) file for more details.

---

### 👨‍💻 Author
Developed with ❤️ by **[Vivek Awasthi](https://github.com/vivekawasthi2007)**.
