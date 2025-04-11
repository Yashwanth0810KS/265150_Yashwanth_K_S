import uuid

# Here iam writing only the to_dict and from_dict because the responsibility of employee.py is
# to handle single task not multiple task


class Employee():

    def __init__(self, id: None, name:str, department:str, designation:str, gross_salary:float, tax:float, 
                 bonus:float):
        self.id = id if id else str(uuid.uuid4())
        self.name = name
        self.department = department
        self.designation = designation
        self.gross_salary = gross_salary
        self.tax = tax
        self.bonus = bonus
        self.net_salary = self.gross_salary - self.tax + self.bonus


    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "department": self.department,
            "designation": self.designation,
            "gross_salary": self.gross_salary,
            "tax": self.tax,
            "bonus": self.bonus,
            "net_salary": self.net_salary
        }
    
# here iam using class method because if in case we convert the Task class into a subclass then it will not work in the same way so,
# it should clearly signals that it is creating an object not work on existing one
    @classmethod
    def from_dict(cls, data):
        return cls(
            id = data["id"],
            name = data["name"],
            department = data["department"],
            designation = data["designation"],
            gross_salary = data["gross_salary"],
            tax = data["tax"],
            bonus = data["bonus"]
        )