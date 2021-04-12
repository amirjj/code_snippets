
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

        

class Accountant(Employee):
    pass
    
# print(help(Accountant))

class Developer(Employee):
    
    def __init__(self, name, payment, pl):
        super().__init__(name, payment)
        self.pl = pl
    
    
class Manager(Employee):
    def __init__(self, name, payment, employee = None):
        super().__init__(name, payment)
        if employee is None:
            self.employee = []
        else:
            self.employee = employee
    
    def add_emp(self, emp):
        if emp not in self.employee:
            self.employee.append(emp)
            
    def delete_emp(self, emp):
        if emp in self.employee:
            self.employee.remove(emp)
            
    def print_emps(self):
        for em in self.employee:
            print(em.name)
            
    
    

d1 = Developer("amir", 40000, "python")
d2 = Developer("ali", 40000, "python")


m1 = Manager("john", 400000, [d1])
print(m1.name)
m1.print_emps()
m1.add_emp(d2)
print('-----')
m1.print_emps()
m1.delete_emp(d1)
print('-----')
m1.print_emps()

# check if an object is an instance of a class
print(isinstance(m1, Manager))
print(isinstance(m1, Employee))
print(isinstance(m1, Developer))
print('-----')
print(isinstance(Manager, Employee))
print('-----')
print(issubclass(Manager, Employee))
print(issubclass(Employee, Manager))
print(issubclass(m1, Manager))