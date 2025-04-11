import unittest
import uuid
import random
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from employee import Employee

name = "Partha"

def random_department():
    return random.choice(["Engineering", "HR", "Finance", "Marketing", "Sales"])

def random_designation():
    return random.choice(["Developer", "Manager", "Analyst", "Recruiter", "Lead"])

def random_salary():
    return random.randint(50000, 150000)

def random_tax():
    return random.randint(5000, 30000)

def random_bonus():
    return random.randint(2000, 20000)

class TestEmployee(unittest.TestCase):

    def test_employee_creation(self):
        department = random_department()
        designation = random_designation()
        gross_salary = random_salary()
        tax = random_tax()
        bonus = random_bonus()

        e = Employee(
            id=None,
            name=name,
            department=department,
            designation=designation,
            gross_salary=gross_salary,
            tax=tax,
            bonus=bonus
        )

        self.assertEqual(e.name, name)
        self.assertEqual(e.department, department)
        self.assertEqual(e.designation, designation)
        self.assertEqual(e.gross_salary, gross_salary)
        self.assertEqual(e.tax, tax)
        self.assertEqual(e.bonus, bonus)
        self.assertEqual(e.net_salary, gross_salary - tax + bonus)
        self.assertTrue(e.id)

    def test_to_dict(self):
        department = random_department()
        designation = random_designation()
        gross_salary = random_salary()
        tax = random_tax()
        bonus = random_bonus()
        emp_id = str(uuid.uuid4())

        e = Employee(
            id = emp_id,
            name = name,
            department = department,
            designation = designation,
            gross_salary = gross_salary,
            tax = tax,
            bonus = bonus
        )

        emp_dict = e.to_dict()

        self.assertEqual(emp_dict["id"], emp_id)
        self.assertEqual(emp_dict["name"], name)
        self.assertEqual(emp_dict["department"], department)
        self.assertEqual(emp_dict["designation"], designation)
        self.assertEqual(emp_dict["gross_salary"], gross_salary)
        self.assertEqual(emp_dict["tax"], tax)
        self.assertEqual(emp_dict["bonus"], bonus)
        self.assertEqual(emp_dict["net_salary"], gross_salary - tax + bonus)

    def test_from_dict(self):
        department = random_department()
        designation = random_designation()
        gross_salary = random_salary()
        tax = random_tax()
        bonus = random_bonus()
        emp_id = str(uuid.uuid4())

        data = {
            "id": emp_id,
            "name": name,
            "department": department,
            "designation": designation,
            "gross_salary": gross_salary,
            "tax": tax,
            "bonus": bonus
        }

        e = Employee.from_dict(data)

        self.assertEqual(e.id, emp_id)
        self.assertEqual(e.name, name)
        self.assertEqual(e.department, department)
        self.assertEqual(e.designation, designation)
        self.assertEqual(e.gross_salary, gross_salary)
        self.assertEqual(e.tax, tax)
        self.assertEqual(e.bonus, bonus)
        self.assertEqual(e.net_salary, gross_salary - tax + bonus)

if __name__ == "__main__":
    unittest.main()
