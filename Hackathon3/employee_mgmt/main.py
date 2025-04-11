# Now lets try interacting with the user
# lets try showing the menu like add, view, delet, complete
# lets take help of taskmanager and storage.py for performing operations
from employee_manager import EmployeeManager
from storage import Storage
 
def display_employee(employees):
    if not employees:
        print("No employees found.")
    for e in employees:
        print(f"Id: {e.id}, Name: {e.name}, Department: {e.department}, Designation: {e.designation}, Gross_salary: {e.gross_salary}, Tax: {e.tax}, Bonus: {e.bonus}, Net_salary: {e.net_salary}")


def main():
    # Here iamcreating an object instance
    manager = EmployeeManager()  
    store = Storage()            

    # Loading the  saved employees from storage
    saved_employee = store.load()
    manager.load_employee(saved_employee)

    while True:
        print("\n==== Employee Management CLI Application MENU ====")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee By Id")
        print("4. Delete Employee")
        print("5. Exit")

        # The below are the choices that performs different task
        choice = input("Choose an option: ").strip()

        # Add Employee
        if choice == '1':
            try:    
                name = input("Enter employee name: ")
                department = input("Enter employee department: ")
                designation = input("Enter employee designation: ")
            except NameError:
                print("Please enter name, department and designation")
                return
            try:
                gross_salary = float(input("Enter employee gross_salary in lpa: "))
                tax = float(input("Enter employee tax: "))
                bonus = float(input("Enter employee bonus: "))

            except ValueError:
                print("Please enter valid numbers for salary, tax, bonus, and net salary.")
                return

            if name.strip():
                employee = manager.add_employee(name.strip(), department.strip(), designation.strip(), gross_salary, tax, bonus)
                store.save(manager.to_dict_list())
                print(f"Employee added with ID: {employee.id}")
            else:
                print("Employee name cannot be empty")

        # View Employees
        elif choice == '2':
            display_employee(manager.view_all_employee())

        # Search Employee By Id
        elif choice == '3':
            eid = input("Enter the employee id to search: ")
            if manager.search_employee(eid):
                print("Employee Id found")
            else:
                print("Employee ID not found")

        # Delete Employee
        elif choice == '4':
            eid = input("Enter the Employee id to delete: ")
            if manager.delete_employee(eid):
                store.save(manager.to_dict_list())
                print(f"Employee with ID {eid} deleted.")
            else:
                print("Employee ID not found")

        # Exit
        elif choice == '5':
            print("Good bye!")
            break
        else:
            print("Invalid choice, please choose a valid option.")

if __name__ == "__main__":
    main()