# else clause will be triggered only when NO break statement encountered

my_list = [2, 4, 6, 8, 9]

for num in my_list:
    if num % 2 != 0:
        break
else:
    print("All numbers are Even")


