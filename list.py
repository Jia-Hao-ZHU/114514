my_list = []
for i in range (9):
    my_list.append(-113)
for num in my_list:
    print (num)
for i in range(len(my_list)):
    print(my_list[i])

import random
my_list = []
for _ in range(10):
    my_list.append(random.randint(1, 100))
for i in range(len(my_list)):
    print(my_list[i])


first = (input(" whats ur first name:"))
last = (input(" whats ur last name:"))
file_name = (input(" whats the name of the file:"))

import random 
grades = []
for i in range(5):
    grades. append(random.randint(1, 100))
for i in range(len(grades)):
    print( first, last, file_name)
    print(grades[i])


import random
random_list = [random.randint(1, 50) for _ in range(10)]
print("List of values:")
for value in random_list:
    print(value)
user_input = int(input("Enter an integer to search for: "))
found = False 
for value in random_list:
    if value == user_input:
        print(f"{user_input} is in the list.")
        found = True


import random
random_list = [random.randint(1, 50) for _ in range(10)]
print("List of values:")
for value in random_list:
    print(value)
user_input = int(input("Enter an integer to search for: "))
count = 0
for value in random_list:
    if value == user_input:
        count += 1
print(f"The number {user_input} was found {count} time(s) in the list.")



import random
random_list = [random.randint(1,50) for i in range(10)]
print("list of num:")
for value in random_list:
    print(value)

user_input = int(input("enter a num to search:"))
found = False
for vaalue in random_list: 
    if value == user_input:
        print(f"{user_input} is in the list.")
        found = True
if not found:
    print(f"{user_input} is not in the list.")



import random
random_list = [random.randint(1, 100) for _ in range(10)]

print("List of values:")
for value in random_list:
    print(value)

largest_value = random_list[0]
for value in random_list:
    if value > largest_value:
        largest_value = value

print(f"The largest value in the list is: {largest_value}")


import random
random_list = [random.randint(1,100) for i in range(10)]
print("list of the num")
for value in random_list:
    print(value)

    big_value = random_list[0]
    for value in random_list:
        if value > big_value:
            big_value = value

big_value = random_list[0]
largest_index = [0] 

for i in range(len(random_list)):
    if random_list[i] > big_value:
        big_value = random_list[i]
        largest_index = i

print(f"largest index is {largest_index}")



animal_string = "monkey bat cat dog"
animal_list = animal_string.split(" ")

print("Animal names:")
for animal in animal_list:
    print(animal)
