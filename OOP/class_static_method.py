# Regular methods in class gets "instance" (self) as its first argument
# class methods get "class" as its first argument
# to change a regular method to class method add @classmethod decorator

class Employee:
    
    raise_amount = 1.04
    num_of_emp = 0
    
    def __init__(self, name, payment):
        self.name = name
        self.payment = payment
        
        # we need to use Employee, because for creating any new employee we need to add 1 num_of_emp
        # for all instances
        Employee.num_of_emp += 1

    # regular method
    def apply_raise(self):
        # we need to access raise_amount either by self or by classname
        self.payment = self.payment * self.raise_amount
        
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
        
    # Use classmethod as an alternative constructor 
    @classmethod
    def from_string(cls, user_str):
        name, payment = user_str.split("-")
        return cls(name, payment)
        
    # static method
    # just like normal function but we add them to the class because they have logical connection to class
    # rule of thumb: if you don't use self or cls anywhere in function it should be staticmethod
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


e1 = Employee("amir", 50000)
e2 = Employee("hasan", 50000)
print(Employee.raise_amount)  
print(e1.raise_amount)  
print(e2.raise_amount)  
e1.set_raise_amount(1.09)
print(Employee.raise_amount)  
print(e1.raise_amount)  
print(e2.raise_amount)  

e3 = Employee.from_string("John-30000")
print(e3.payment)
###########################
import datetime
day = datetime.date(2019, 7, 1)

print(Employee.is_workday(day))
