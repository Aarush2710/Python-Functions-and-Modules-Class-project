def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
print("Select operation:")

print("1. Add")

print("2. Subtract")

print("3. Multiply")

print("4. Divide")
num1=int(input("Enter the first number  "))
num2=int(input("Enter the second number  "))
choice=str(input("Enter your choice  "))
if choice == "1":
    print(add(num1,num2))
elif choice == "2":
     print(sub(num1,num2))
elif choice == "3":
     print(mul(num1,num2))
elif choice == "4":
     print(div(num1,num2))
else:
    print("Invaild")

