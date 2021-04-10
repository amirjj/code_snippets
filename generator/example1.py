
def square(numbers):
	for num in numbers:
		yield num * num

my_nums = square([1, 2, 3, 4, 5])
print(my_nums)
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))

# for num in my_nums:
# 	print(num)

nums = [1, 2, 3, 4, 5]
my_list_comprehention = [num*num for num in nums]
print(my_list_comprehention)

my_generator = (num*num for num in nums)
print(my_generator)
print(next(my_generator))

print(list(my_generator))

