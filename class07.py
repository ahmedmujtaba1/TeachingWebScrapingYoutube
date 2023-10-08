# # Function
# def hello_world(name):
#     global author_name
#     author_name = "Saad"
#     print(f"Hello {name}!")

# hello_world("Ahmed")
# print(author_name)
# hello_world("World")

# CALCULATOR

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

def calculator(num1, num2, operator):
    if operator == "+":
        print(f"[+] The result after adding is {num1} + {num2} = {add(num1,num2)}")
    elif operator == "-":
        print(f"[+] The result after subtracting is {num1} - {num2} = {subtract(num1,num2)}")
    elif operator == "x" or operator == "*":
        print(f"[+] The result after multiplying is {num1} x {num2} = {multiply(num1,num2)}")
    elif operator == "/":
        print(f"[+] The result after dividing is {num1} / {num2} = {divide(num1,num2)}")

print("[+] Welcome to Mustafa Calculator")
n01 = int(input("[+] Enter Your First Number : "))
n02 = int(input("[+] Enter Your Second Number : "))
oper = input("[+] Enter your operator: ")
calculator(n01,n02,oper)


#OOPS
