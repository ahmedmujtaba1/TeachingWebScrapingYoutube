class Calculator:
    def __init__(self, num1, num2, operator):
        self.num1 = num1
        self.num2 = num2
        self.operator = operator

    def add(self):
        return self.num1 + self.num2
    
    def subtract(self):
        return self.num1 - self.num2
    
    def multiply(self):
        return self.num1 * self.num2
    
    def divide(self):
        return self.num1 / self.num2

    def result(self):
        if self.operator == "+":
            print(f"[+] The result after adding is {self.num1} + {self.num2} = {self.add()}")
        elif self.operator == "-":
            print(f"[+] The result after subtracting is {self.num1} - {self.num2} = {self.subtract()}")
        elif self.operator == "x" or self.operator == "*":
            print(f"[+] The result after multiplying is {self.num1} x {self.num2} = {self.multiply()}")
        elif self.operator == "/":
            print(f"[+] The result after dividing is {self.num1} / {self.num2} = {self.divide()}")

n01 = int(input("[+] Enter Your First Number : "))
n02 = int(input("[+] Enter Your Second Number : "))
oper = input("[+] Enter your operator: ")
calc = Calculator(n01,n02,oper)
calc.result()