# Device Management API

This is a **Django REST Framework (DRF) project** for managing users and devices with **JWT authentication**, **role-based access control**, and **API documentation using DRF Spectacular**.

---

## Features

1. **Authentication**

   * **JWT-based login, register, change password, and logout** for secure authentication.
   * Token is required to access protected endpoints.

2. **User Roles**

   * **Admin**, **Staff**, **User**.
   * **Role-based access control**:

     * Users can only view their own devices.
     * Admins and Staff can add, edit, delete, and view all devices.

3. **User Profile**

   * View and update profile information.

4. **Device Management**

   * Add, edit, list, and delete devices based on user role.

5. **API Documentation**

   * Fully documented with **DRF Spectacular**.
   * Swagger UI available at: `/api/schema/swagger-ui/`

---

## Project Setup

Follow these steps to run the project locally:

### 1. Clone the repository

```bash
git clone <repository_url>
cd <project_folder>
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

* **Windows:**

```bash
venv\Scripts\activate
```

* **Linux / Mac:**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Variables

Create a `.env` file in the project root:

```
SECRET_KEY=your_django_secret_key
DEBUG=True
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432

# JWT Settings
SIMPLE_JWT_ACCESS_TOKEN_LIFETIME=1d
SIMPLE_JWT_REFRESH_TOKEN_LIFETIME=7d
```

> **Note:** Never push `.env` to GitHub.

### 5. Database Setup

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a superuser

```bash
python manage.py createsuperuser
```

### 7. Run the server

```bash
python manage.py runserver
```

Open API at: `http://127.0.0.1:8000/`
Swagger UI docs: `http://127.0.0.1:8000/api/schema/swagger-ui/`


## Notes

* Use **JWT Token** in headers for protected endpoints:

  ```
  Authorization: Bearer <your_jwt_token_here>
  ```
* Role-based access ensures secure operations based on user type.
* API docs are automatically generated with DRF Spectacular.

---

## License

This project is **open-source** and free to use.

