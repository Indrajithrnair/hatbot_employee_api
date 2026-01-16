# Employee Management API

A robust REST API built with Django and Django REST Framework for managing company employees. This project allows for secure CRUD operations, filtering, and pagination, protected by JWT authentication.

## Features

- **CRUD Operations**: Create, Read, Update, and Delete employees.
- **Authentication**: Secure JWT (JSON Web Token) authentication for all write and read operations.
- **Filtering**: Filter employees by `department` and `role`.
- **Pagination**: Results are paginated (10 items per page) to ensure performance.
- **Validation**: Strict validation for required fields and unique email constraints.
- **Testing**: Comprehensive unit tests covering 100% of the endpoints.

## Tech Stack

- **Language**: Python 3.x
- **Framework**: Django 6.x
- **API Toolkit**: Django REST Framework (DRF)
- **Authentication**: SimpleJWT
- **Database**: SQLite (Default)

---

## Local Setup Instructions

Follow these steps to get the project running on your local machine.

### 1. Prerequisites
Ensure you have Python installed.

### 2. Install Dependencies
Navigate to the project directory and install the required packages:

```bash
pip install -r requirements.txt
```

### 3. Database Migration
Initialize the database tables:

```bash
python manage.py migrate
```

### 4. Create Admin User (Optional)
To access the Django Admin panel:

```bash
python manage.py createsuperuser
```

### 5. Run the Server
Start the development server:

```bash
python manage.py runserver
```
The API is now accessible at `http://127.0.0.1:8000/`.

---

## API Documentation

### Authentication
**All endpoints require a Bearer Token.**

1.  **Obtain Token**
    *   **Endpoint**: `POST /api/token/`
    *   **Body**:
        ```json
        {
            "username": "your_username",
            "password": "your_password"
        }
        ```
    *   **Response**: Returns `access` and `refresh` tokens.
    *   **Usage**: Add header `Authorization: Bearer <access_token>` to all subsequent requests.

### Endpoints

#### 1. List & Create Employees
*   **URL**: `/api/employees/`
*   **GET**: Returns a paginated list of employees.
    *   **Query Params**:
        *   `?page=2` (Pagination)
        *   `?department=HR` (Filter)
        *   `?role=MANAGER` (Filter)
*   **POST**: Create a new employee.
    *   **Body**:
        ```json
        {
            "name": "John Doe",
            "email": "john.doe@example.com",
            "department": "HR",
            "role": "MANAGER"
        }
        ```

#### 2. Retrieve, Update, & Delete Employee
*   **URL**: `/api/employees/<id>/`
*   **GET**: Get details of a single employee.
*   **PUT**: Update employee details.
    *   **Body**: (Same as POST)
*   **DELETE**: Remove an employee (Returns `204 No Content`).

---

## Running Tests

This project includes a fully automated test suite checking authentication, CRUD logic, and edge cases.

Run the tests using:

```bash
python manage.py test app
```
