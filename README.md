# Device Management API

This is a **Django REST Framework (DRF) project** for managing users and devices with **JWT authentication**, **role-based access control**, and **API documentation using DRF Spectacular**.
Additionally, this project integrates **bKash payment gateway** for testing payment flows.

---

## Features

1. **Authentication**

   * JWT-based login, registration, change password, and logout for secure authentication.
   * Tokens are required to access protected endpoints.

2. **User Roles**

   * **Admin**, **Staff**, **User**
   * Role-based access control:

     * Users can only view their own devices.
     * Admins and Staff can add, edit, delete, and view all devices.

3. **User Profile**

   * View and update profile information.

4. **Device Management**

   * Add, edit, list, and delete devices based on user role.

5. **Payment Gateway**

   * Integration with **bKash tokenized checkout** for creating and executing payments.
   * **Demo credentials for testing**:

     * bKash PIN: `12121`
     * OTP: `123456`
   * Callback URLs handle payment success, failure, and cancellation.
   * Payments update the database automatically when completed.

6. **API Documentation**

   * Fully documented using **DRF Spectacular**
   * Swagger UI available at `/api/schema/swagger-ui/`

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

```env
SECRET_KEY=your_django_secret_key
DEBUG=True

# Database
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432

# JWT Settings
SIMPLE_JWT_ACCESS_TOKEN_LIFETIME=1d
SIMPLE_JWT_REFRESH_TOKEN_LIFETIME=7d

# bKash Sandbox Settings (Demo)
BKASH_USERNAME=sandboxTokenizedUser02
BKASH_PASSWORD=sandboxTokenizedUser02@12345
BKASH_APP_KEY=your_app_key
BKASH_APP_SECRET=your_app_secret
BKASH_CALLBACK_URL=http://127.0.0.1:8000/api/bkash/callback/
```

> **Note:** Never push `.env` to GitHub.

---

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

---

## API Usage Notes

* Use **JWT Token** in headers for protected endpoints:

```http
Authorization: Bearer <your_jwt_token_here>
```

* Role-based access ensures secure operations based on user type.
* **bKash Payment Flow**:

  1. Generate a **grant token**.
  2. Create a **payment request** with amount, currency, and invoice number.
  3. Execute payment after the user completes it.
  4. Payment callback updates the database and redirects the user to a success or failure page.

---

## License

This project is **open-source** and free to use.
