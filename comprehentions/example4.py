n = [1,2,3,4,5,6,7,8]

#Generator
def list_gen(n):
	for i in n:
		yield i * i

my_gen = list_gen(n)
for el in my_gen:
	print(el)

#Generator comprehention

my_gen = (i*i for i in n)

for el in my_gen:
	print(el)
