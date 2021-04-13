# with this feature we change the code while other developers 
# doesn't feel any change and they don't need to change other parts of codes
class Employee:
    
    def __init__(self, name, payment):
        self.name = name
        self.payment = payment
    
        
    @property
    def email(self):
        return f"{self.name}@gmail.com"
        
    @email.setter
    def email(self, name):
        self.name = name
        
    @email.deleter
    def email(self):
        self.name = None


        
e1 = Employee("John", 10000)
print(e1.name)
print(e1.email)
e1.email = "amir"
print(e1.name)
print(e1.email)
del e1.email
print(e1.name)
print(e1.email)

