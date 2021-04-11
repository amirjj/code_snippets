# int separator for more readability
var1 = 10_234_222
var2 = 10234222

print(var1)
print(var2)

print(type(var1))
print(type(var2))

print(var1+1)
print(var2+1)
    
print("########################################")

# eval -> evaluating expressions exec -> for executing statements
# Helps to write dynamic code
# exec is a basically a python interpretor (you can write a python code to solve a problem)
# best use cased (https://mail.python.org/pipermail/tutor/2015-February/104238.html)
a = 3
res = eval('a + 2')
print("res:", res)


res2 = exec('c = a + 3')
print("c:", c)

print("########################################")
# Ellipses ... is a built-in constant 

# use like pass
def f1():
    ...
    
def f2():
    pass

for _ in range(10):
    ...
    
# Alternative to None
def what_num(n = ...):
    if n is ...:
        print("No argument passed")
        
what_num()


    