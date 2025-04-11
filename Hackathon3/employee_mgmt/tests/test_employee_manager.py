import unittest
import uuid
import random
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from employee_manager import EmployeeManager
from employee import Employee

name = "Partha"

def random_department():
    return random.choice(["HR", "Engineering", "Marketing", "Finance", "Sales"])

def random_designation():
    return random.choice(["Developer", "Manager", "Analyst", "Executive", "Intern"])

def random_salary():
    return random.randint(50000, 150000)

def random_tax():
    return random.randint(5000, 30000)

def random_bonus():
    return random.randint(1000, 20000)

class TestEmployeeManager(unittest.TestCase):

    def setUp(self):
        self.manager = EmployeeManager()

    def test_add_employee(self):
        gross = random_salary()
        tax = random_tax()
        bonus = random_bonus()
        emp = self.manager.add_employee(
            name=name,
            department=random_department(),
            designation=random_designation(),
            gross_salary=gross,
            tax=tax,
            bonus=bonus
        )
        self.assertEqual(len(self.manager.employees), 1)
        self.assertEqual(emp.name, name)
        self.assertEqual(emp.net_salary, gross - tax + bonus)

    def test_view_all_employee(self):
        self.manager.add_employee(
            name, random_department(), random_designation(),
            random_salary(), random_tax(), random_bonus()
        )
        employees = self.manager.view_all_employee()
        self.assertEqual(len(employees), 1)
        self.assertIsInstance(employees[0], Employee)

    def test_search_employee_success(self):
        emp = self.manager.add_employee(
            name, random_department(), random_designation(),
            random_salary(), random_tax(), random_bonus()
        )
        found = self.manager.search_employee(emp.id)
        self.assertIn("Employee found", found)

    def test_search_employee_failure(self):
        with self.assertRaises(ValueError) as ctx:
            self.manager.search_employee("non-existent-id")
        self.assertIn("No employee found", str(ctx.exception))

    def test_delete_employee_success(self):
        emp = self.manager.add_employee(
            name, random_department(), random_designation(),
            random_salary(), random_tax(), random_bonus()
        )
        deleted = self.manager.delete_employee(emp.id)
        self.assertTrue(deleted)
        self.assertEqual(len(self.manager.employees), 0)

    def test_delete_employee_failure(self):
        with self.assertRaises(ValueError) as ctx:
            self.manager.delete_employee("invalid-id")
        self.assertIn("No employee found", str(ctx.exception))

    def test_load_employee(self):
        gross = random_salary()
        tax = random_tax()
        bonus = random_bonus()
        test_dict = [{
            "id": str(uuid.uuid4()),
            "name": name,
            "department": random_department(),
            "designation": random_designation(),
            "gross_salary": gross,
            "tax": tax,
            "bonus": bonus
        }]
        self.manager.load_employee(test_dict)
        self.assertEqual(len(self.manager.employees), 1)
        self.assertEqual(self.manager.employees[0].name, name)

    def test_to_dict_list(self):
        gross = random_salary()
        tax = random_tax()
        bonus = random_bonus()
        emp = self.manager.add_employee(
            name, random_department(), random_designation(),
            gross, tax, bonus
        )
        dict_list = self.manager.to_dict_list()
        self.assertEqual(len(dict_list), 1)
        self.assertEqual(dict_list[0]["name"], name)
        self.assertEqual(dict_list[0]["net_salary"], gross - tax + bonus)

if __name__ == "__main__":
    unittest.main()
