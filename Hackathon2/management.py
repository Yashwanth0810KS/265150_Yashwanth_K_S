import json

class Person():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

class Employee(Person):
    def __init__(self, name, age, gender, emp_id, department, salary):
        super().__init__(name, age, gender)
        self.emp_id = emp_id
        self.department = department
        self.salary = salary

    def get_details(self):
        person_details = super().get_details()
        return f"{person_details}, Emp ID: {self.emp_id}, Department: {self.department}, Salary: Rupees {self.salary}"

    def is_eligible_for_bonus(self):
        return self.salary < 50000
    
    @classmethod
    def from_string(cls, data_string):
        data_part = data_string.split(',')
        if len(data_part) != 6:
            raise ValueError("Please give exactly the (name, age, gender, empid, department, salary)")
        
        name = data_part[0]
        age = int(data_part[1])
        gender = data_part[2]
        emp_id = data_part[3]
        department = data_part[4]
        salary = float(data_part[5])

        return cls(name, age, gender, emp_id, department, salary)

    @staticmethod
    def bonus_policy():
        print("Bonus Policy: Employees with a salary below Rupees 50,000 are eligible for a bonus. "
              "The bonus is calculated based on performance and department-specific targets.")

class Department():
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        if isinstance(employee, Employee):
            self.employees.append(employee)
        else:
            print("Error! The employee is not found.")

    def get_average_salary(self):
        if not self.employees:
            return 0
        total_salary = sum(employee.salary for employee in self.employees)
        return total_salary / len(self.employees)

    def get_all_employee_details(self):
        return [employee.get_details() for employee in self.employees]

    def __repr__(self):
        return f"Department(name={self.name}, employees={len(self.employees)})"

def save_to_json(employees, filename="employee_data.json"):
    employee_data = [
        {
            "name": emp.name,
            "age": emp.age,
            "gender": emp.gender,
            "emp_id": emp.emp_id,
            "department": emp.department,
            "salary": emp.salary
        }
        for emp in employees
    ]
    
    with open(filename, 'w') as json_file:
        json.dump(employee_data, json_file, indent=4)
    print(f"\nEmployee data saved to {filename}")

def load_from_json(filename="employee_data.json"):
    employees = []
    try:
        with open(filename, 'r') as json_file:
            employee_data = json.load(json_file)
            
            # Create Employee objects from the JSON data
            for emp in employee_data:
                employee = Employee(
                    emp['name'],
                    emp['age'],
                    emp['gender'],
                    emp['emp_id'],
                    emp['department'],
                    emp['salary']
                )
                employees.append(employee)
            
            return employees
    
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
        return []

# Group employees by their department
def group_by_department(employees):
    departments = {}
    for emp in employees:
        if emp.department not in departments:
            departments[emp.department] = Department(emp.department)
        departments[emp.department].add_employee(emp)
    return departments

if __name__ == "__main__":
    data_strings = [
        "Alice,30,Female,E101,HR,48000",
        "Bob,28,Male,E102,IT,55000",
        "Charlie,35,Male,E103,HR,60000",
        "Diana,26,Female,E104,IT,47000",
        "Evan,40,Male,E105,Finance,53000"
    ]
    
    employees = [Employee.from_string(s) for s in data_strings]
    
    Employee.bonus_policy()

    print("\nEmployee Details:")
    for emp in employees:
        print(emp.get_details())

    save_to_json(employees)

    print("\nLoading employees from JSON...")
    loaded_employees = load_from_json()

    print("\nGrouping Employees by Department...")
    departments = group_by_department(loaded_employees)

    for dept_name, dept in departments.items():
        print(f"\nDepartment: {dept_name}")
        for emp_details in dept.get_all_employee_details():
            print(emp_details)
        print(f"Average Salary: Rupees {dept.get_average_salary():.2f}")
