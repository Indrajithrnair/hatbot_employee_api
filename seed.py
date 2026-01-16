import os
import django
import random

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from app.models import Employee

def seed_data():
    departments = ["HR", "ENGINEERING", "SALES"]
    roles = ["MANAGER", "DEVELOPER", "ANALYST"]

    print("Deleting existing employees...")
    Employee.objects.all().delete()  # optional: reset

    employees = []
    print("Creating 30 new employees...")
    for i in range(1, 31):  # create 30 employees
        employees.append(
            Employee(
                name=f"Employee {i}",
                email=f"employee{i}@example.com",
                department=random.choice(departments),
                role=random.choice(roles)
            )
        )

    Employee.objects.bulk_create(employees)

    print("Successfully seeded 30 employees")

if __name__ == '__main__':
    seed_data()
