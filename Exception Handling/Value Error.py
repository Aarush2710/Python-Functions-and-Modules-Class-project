try:
    age=int(input("Enter A Number  "))
    print(age)
except ValueError as ve:
    print("Only numbers re allowed")
finally:
    print("Code executed sucessfully")