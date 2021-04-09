# Dictionary comprehention

names = ['ali', 'hasan', 'yaser', 'amir']
last_names = ['mj', 'mohammady', 'jj']

print(list(zip(names, last_names)))

my_dict = {}

for name, l_name in zip(names, last_names):
	my_dict[name] = l_name
print(my_dict)

my_dict = {name:l_name for name, l_name in zip(names, last_names) if name != 'hasan'}
print(my_dict)


