class Employee:
    def __init__(self, name, emp_id, dept, salary):
        self.name = name
        self.emp_id = emp_id
        self.dept = dept
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}, ID: {self.emp_id}, Department: {self.dept}, Salary: {self.salary}")

    # Method to update salary
    def update_salary(self, increment):
        self.salary += increment


# ----------------------------
# Function to update salaries
# ----------------------------
def update_department_salary(employee_list, department, increment):
    for emp in employee_list:
        if emp.dept.lower
