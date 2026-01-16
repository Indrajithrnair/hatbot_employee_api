# 🚀 Live Demo Walkthrough Checklist

Use this guide during your presentation to ensure you cover all requirements systematically.

## 1. 🎤 Introduction (1-2 mins)
- **Goal**: Briefly explain the project.
- **Talking Points**:
    - "This is a RESTful API for Employee Management."
    - "It handles CRUD operations, Data Validation, and JWT Authentication."
    - "I used Django REST Framework (DRF) because it's scalable and follows standard web practices."
    - "I also implemented Pagination and Filtering."

---

## 2. 🔐 Authentication (Show Security)
*Switch to Postman (or your API testing tool)*

### Step 1: Try to Access without Token
- **Action**: GET `http://127.0.0.1:8000/api/employees/` (No Headers)
- **Result**: `401 Unauthorized`.
- **Comment**: "As you can see, the API is secure by default."

### Step 2: Get a Token
- **Action**: POST `http://127.0.0.1:8000/api/token/`
- **Body**:
  ```json
  {
      "username": "admin",
      "password": "admin"
  }
  ```
- **Result**: `200 OK` with `access` and `refresh` tokens.
- **Action**: Copy the `access` token.
- **Comment**: "I'm now authenticated via JWT. I will use this token for all subsequent requests."

---

## 3. 🛠️ CRUD Operations Demo

### A. Create Employee (POST)
- **Endpoint**: `POST /api/employees/`
- **Headers**: `Authorization: Bearer <your_token>`
- **Body (Valid)**:
  ```json
  {
      "name": "Sarah Connor",
      "email": "sarah@skynet.com",
      "department": "ENGINEERING",
      "role": "DEVELOPER"
  }
  ```
- **Result**: `201 Created`.
- **Comment**: "The employee is successfully created."

### B. Validation Check (Duplicate Email)
- **Action**: Send the **exact same request** again.
- **Result**: `400 Bad Request` -> `"Email already exists..!"`
- **Comment**: "The API enforces data integrity. Duplicate emails are not allowed."

### C. List Employees + Pagination + Filter (GET)
- **Endpoint**: `GET /api/employees/`
- **Result**: JSON list of employees in `results` array with `count`, `next`, `previous` fields.
- **Comment**: "Here is the paginated list."

- **Action (Filter)**: `GET /api/employees/?department=HR`
- **Result**: Only employees with `department: "HR"`.
- **Comment**: "I can easily filter results by department."

### D. Retrieve Single Employee (GET)
- **Endpoint**: `GET /api/employees/<ID of Sarah>/`
- **Result**: `200 OK` with Sarah's details.

- **Action (Error Case)**: `GET /api/employees/9999/`
- **Result**: `404 Not Found`.
- **Comment**: "The API correctly identifies non-existent resources."

### E. Update Employee (PUT)
- **Endpoint**: `PUT /api/employees/<ID of Sarah>/`
- **Body**: Change `role` to `MANAGER`.
  ```json
  {
      "name": "Sarah Connor",
      "email": "sarah@skynet.com",
      "department": "ENGINEERING",
      "role": "MANAGER"
  }
  ```
- **Result**: `200 OK` showing updated role.

### F. Delete Employee (DELETE)
- **Endpoint**: `DELETE /api/employees/<ID of Sarah>/`
- **Result**: `204 No Content` (Empty response).
- **Verification**: Try to GET that ID again -> `404 Not Found`.

---

## 4. 📝 Code Review (If asked)
- **Models**: Show `app/models.py` (Choices, Unique Email constraint).
- **Serializers**: Show `app/serializers.py` (Custom validation methods).
- **Tests**: Briefly show `app/tests.py` and mention "I have full test coverage."
- **Run Tests**:
  ```bash
  python manage.py test app
  ```

## 5. 🏁 Conclusion
- "In summary, the API is fully functional, creates secure endpoints, and handles edge cases like validation and missing data correctly. It's ready for production use."
