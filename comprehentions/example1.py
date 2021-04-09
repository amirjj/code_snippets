n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


my_list = [el for el in n]
print(my_list)

my_list = [el*el for el in n]
print(my_list)

my_list = map(lambda el: el*el ,n)
print(list(my_list))

my_list = [el for el in n if el % 2 ==0]
print(my_list)

my_list = filter(lambda el: el % 2 == 0 , n)
print(list(my_list))

my_list = [(letter, num) for letter in "abcd" for num in range(4)]
print(my_list)


