# https://docs.python.org/3/reference/datamodel.html#special-method-names

# from Exception import TypeError

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
        
    # unambiguous representation of and object used for logging and debugging 
    def __repr__(self):
        return f"Employee({self.name}, {self.payment})"
    
    # more readable representation of an object (display to enduser)
    def __str__(self):
        return self.name
            
        
    def __add__(self, other):
        if isinstance(other, Employee):
            return self.payment + other.payment
        raise TypeError("pass Employee object")
        
        
e1 = Employee("amir", 50000)
e2 = Employee("hasan", 50000)
print(e1 + e2)

print(e1)
print(repr(e2))
print(str(e2))
print(e2.__repr__())
print(e2.__str__())
###################
print(1+2)
print(int.__add__(1,2))
print("a"+"b")
print(str.__add__("a","b"))
#####################
print(len("test"))
print("test".__len__())


