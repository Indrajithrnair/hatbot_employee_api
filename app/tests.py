from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase

from .models import Employee


class EmployeeAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123"
        )

        response = self.client.post(
            "/api/token/",
            {"username": "testuser", "password": "testpass123"},
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.token = response.data["access"]

        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {self.token}"
        )

        self.employee = Employee.objects.create(
            name="John Doe",
            email="john@example.com",
            department="HR",
            role="MANAGER"
        )

    def test_auth_required(self):
        self.client.credentials()
        response = self.client.get("/api/employees/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_employee(self):
        data = {
            "name": "Alice",
            "email": "alice@example.com",
            "department": "SALES",
            "role": "ANALYST"
        }
        response = self.client.post("/api/employees/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Employee.objects.count(), 2)

    def test_duplicate_email(self):
        data = {
            "name": "Another John",
            "email": "john@example.com"
        }
        response = self.client.post("/api/employees/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_employees(self):
        response = self.client.get("/api/employees/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("results", response.data)

    def test_get_employee(self):
        response = self.client.get(f"/api/employees/{self.employee.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["email"], "john@example.com")

    def test_get_invalid_employee(self):
        response = self.client.get("/api/employees/999/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_employee(self):
        data = {
            "name": "John Updated",
            "email": "john@example.com",
            "department": "ENGINEERING",
            "role": "DEVELOPER"
        }
        response = self.client.put(
            f"/api/employees/{self.employee.id}/",
            data,
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.employee.refresh_from_db()
        self.assertEqual(self.employee.role, "DEVELOPER")

    def test_delete_employee(self):
        response = self.client.delete(f"/api/employees/{self.employee.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Employee.objects.count(), 0)

    def test_pagination_limit(self):
        for i in range(15):
            Employee.objects.create(
                name=f"Emp {i}",
                email=f"emp{i}@example.com"
            )

        response = self.client.get("/api/employees/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 10)
