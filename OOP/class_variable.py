# Apply a variable too all instances (shared on all instances)

class Employee:
    
    raise_amount = 1.04
    num_of_emp = 0
    
    def __init__(self, name, payment):
        self.name = name
        self.payment = payment
        
        # we need to use Employee, because for creating any new employee we need to add 1 num_of_emp
        # for all instances
        Employee.num_of_emp += 1
        
    def apply_raise(self):
        # we need to access raise_amount either by self or by classname
        self.payment = self.payment * self.raise_amount
        
  
print("Num:",Employee.num_of_emp)  
e1 = Employee("amir", 50000)
e2 = Employee("hasan", 50000)
print("Num:",Employee.num_of_emp)

print(e1.__dict__)
print(Employee.__dict__)
e1.raise_amount = 1.07
print(e1.__dict__)
print("########")

e1.apply_raise()
print(e1.payment)
Employee.raise_amount = 1.05
print(e1.raise_amount)
print(e2.raise_amount)
print(Employee.raise_amount)
  
  
print("##############")
e3 = Employee("e3", 40000)
e4 = Employee("e4", 40000)
print(e3.raise_amount)
print(e4.raise_amount)
print(e3.__dict__)
print(e4.__dict__)
e3.apply_raise()
print(e3.__dict__)
print(e4.__dict__)
e3.raise_amount = 1.06
print(e3.__dict__)
print(e4.__dict__)

print(e3.raise_amount)
print(e4.raise_amount)
print(Employee.raise_amount)

print("Num:",Employee.num_of_emp)
print("Num:",e3.num_of_emp)
