# Define the Company class (main class)
class Company:
    def __init__(self, name, city, mobile_no):
        self.name = name
        self.city = city
        self.mobile_no = mobile_no

    def display_company_details(self):
        print(f"Company Name: {self.name}")
        print(f"City: {self.city}")
        print(f"Mobile No: {self.mobile_no}")

# Define the Employee class (sub class) that inherits from Company
class Employee(Company):
    def __init__(self, name, city, mobile_no, emp_name, designation, salary):
        super().__init__(name, city, mobile_no)  # Call the Company class constructor
        self.emp_name = emp_name
        self.designation = designation
        self.salary = salary

    def display_employee_details(self):
        self.display_company_details()  # Call the method from the Company class
        print(f"Employee Name: {self.emp_name}")
        print(f"Designation: {self.designation}")
        print(f"Salary: {self.salary}")

# Create an object of the Employee class
emp1 = Employee("DJ Corporation", "Rajkot", "9601776480", "dhambha", "Software Engineer", 50000)

# Display employee details using the object
emp1.display_employee_details()