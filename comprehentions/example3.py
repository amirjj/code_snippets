n = [1,1,1,1,1,2,3,4,5,6,6,6,6,6,7,8,9]

#Set comprehention
my_set = set(n)
print(my_set)

my_set = set()
for el in n:
	my_set.add(el)
print(my_set)

print(n)
ali = {el for el in n}
print(ali)
