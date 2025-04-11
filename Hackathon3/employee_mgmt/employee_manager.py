# In the employee_manager iam writing code to handle/manage list of tasks

# So from the problem statement the task that needs to be done by employee_manager are:
# Add new employee ----> creates a new employee and adds to the list
# view employee ---->  Returning the list of employee that are currently there
# search employee by id ----> for this need to find the employee by employee id
# delete employee ----> Here we have to specify the employee id and need to delete or remove it from the employee list
# save/load employee ----> Need to save the employee list which means writing it into a file and load means fetching the data from the file


from employee import Employee
 
 
class EmployeeManager():
    # the below is the constructor method which here is holding the objects created by the 'Task class' inside a list
    def __init__(self):
        self.employees = []
 
    # Now lets add a employee, so for adding a employee we need to specify the name of the employee so lets 
    # try passing an argument in the function to employee input from
    def add_employee(self, name, department, designation, gross_salary, tax, bonus):
        employee = Employee(None, name, department,designation, gross_salary, tax, bonus)
        # Now append it to the employee list which is 'self.tasks'
        self.employees.append(employee)
        # return the employee that is appended
        return employee
   
    # Now lets try fetching/view all the employee that are in the list
    def view_all_employee(self):
        return self.employees
   
    # Now lets fetch a class by its id and mark it as complete
    def search_employee(self, emp_id):
        # for employee in list of employees if the employee that we provide is matched then fetch the 
        # employee or return true else rasie an exception
        for employee in self.employees:
            if employee.id == emp_id:
                return f"Employee found {employee}"
           
        raise ValueError(f"No employee found with {emp_id}, enter the correct id")
   
    # Now lets delete employee by fetching id
    def delete_employee(self, emp_id):
        for employee in self.employees:
            if employee.id == emp_id:
                self.employees.remove(employee)
                return True
           
        raise ValueError(f"No employee found with {emp_id}, enter the correct id")
   
    # Now lets load the employee to a file
    def load_employee(self, emp_dict):
        for ed in emp_dict:
            #converting the dictionary into employee object
            employee = Employee.from_dict(ed)
            #adding to employees list
            self.employees.append(employee)
 
 
    # This will help in converting the data into dictionary format and is helpful in processing the 
    # data to file like json
    def to_dict_list(self):
        return [employee.to_dict() for employee in self.employees]