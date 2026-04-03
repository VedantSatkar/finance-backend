# 💰 Finance Backend API (Django REST Framework)

## 🚀 Project Overview

This project is a **Finance Data Processing Backend System** designed to manage financial records with secure role-based access control and provide meaningful analytics through REST APIs.

The system demonstrates strong backend fundamentals including API design, data modeling, authentication, and data aggregation.

---

## 🎯 Key Highlights

* 🔐 Role-Based Access Control (Admin, Analyst, Viewer)
* 📊 Real-time Financial Analytics
* 🔄 Complete CRUD Operations
* ⚡ Optimized Query Filtering
* 🛡️ Secure JWT Authentication
* 📈 Dashboard Insights with Aggregation

---

## 🛠️ Tech Stack

| Layer     | Technology            |
| --------- | --------------------- |
| Backend   | Django                |
| API Layer | Django REST Framework |
| Database  | SQLite                |
| Auth      | JWT (SimpleJWT)       |

---

## 📂 Features

### 👤 User & Role Management

* Admin → Full access
* Analyst → Read + analytics
* Viewer → Read-only
* Role-based API restrictions

---

### 💰 Financial Records Module

* Create, Read, Update, Delete records
* Fields:

  * Amount
  * Type (Income / Expense)
  * Category
  * Date
  * Notes
* Advanced filtering:

  * By type
  * By category
  * By date range

---

### 📊 Dashboard Analytics

* Total Income
* Total Expenses
* Net Balance
* Category-wise breakdown
* Recent transactions
* Monthly trends (last 30 days)

---

### 🔐 Authentication & Security

* JWT-based authentication
* Protected endpoints
* Token-based access

---

### ⚠️ Validation & Error Handling

* Prevent invalid data (e.g., negative amounts)
* Proper HTTP status responses
* Clean API error messages

---

## 📡 API Endpoints

### 🔑 Authentication

```
POST /api/login/
```

---

### 📁 Financial Records

```
GET    /api/records/
POST   /api/records/
PUT    /api/records/{id}/
DELETE /api/records/{id}/
```

---

### 📊 Dashboard

```
GET /api/dashboard/
```

---

## ⚙️ Run Locally

```bash
git clone https://github.com/VedantSatkar/finance-backend.git
cd finance_backend

python -m venv venv
venv\Scripts\activate

pip install django djangorestframework djangorestframework-simplejwt

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## 🔐 How to Use Authentication

1. Login via:

```
POST /api/login/
```

2. Use token in headers:

```
Authorization: Bearer <your_token>
```

---

## 💡 Design Decisions

* Django chosen for rapid development and built-in admin panel
* DRF for scalable API architecture
* JWT for stateless and secure authentication
* SQLite for simplicity and quick setup

---

## 🚧 Future Improvements

* Pagination
* Search functionality
* Swagger API docs
* Deployment (AWS / Render)

---

## 👨‍💻 Author

**Vedant Satkar**