# databases

fruits = [] # ---> list
fruits = {} # ----> dic
fruits = "apple" # string
fruits = "9" # string
fruits_cont = 1.2  #float
fruits_cont = 2  #int

# pip ---> install packages
#python3 --> pip3

# For installing packages : 
# package : names ----> generate random name

# import names as generate_name


# #  list 
# fruit_list = ["Apple", "Banana"]
# # Error : print('Current Fruits List' + fruit_list) # concatenate (only strings) "+"
# print(f'Current Fruits List {fruit_list}') # format "f"
# new_fruit = input("Please enter a fruit name:\n")
# fruit_list.append(new_fruit) 
# print(f'Updated Fruits List {fruit_list}')


# num_list = [1, 2, 3, 4, 5]
# print(f'Current Numbers List {num_list}')
# num_list.insert(2, "2")
# print(f'Updated Numbers List {num_list}')

num_list = [1, 2, 3, 4, 5]
num_list[1] = "2"
print(num_list) # changing the value of element

num_list.pop(1) # delete element
print(num_list)

# For loops.
# Syntax
# for {variable_name} in {list_name}:
# for {variable_name} in range(len({list_name})):
# 1st way: 
# len() --> for counting elements contain variable (only on list, typle or dict)
# print(len(num_list))

# range() ---> for loop kitni dafa chalega....ok?
