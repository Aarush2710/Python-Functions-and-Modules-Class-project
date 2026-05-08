try:
    num1=int(input("Enter a numertor  "))
    num2=int(input("Enter a denomator  "))
    result=num1/num2
    print("The result is",result)
except ZeroDivisionError:
    print("Dividing with zero is not possible")
except ValueError:
    print("Invaild input")
finally:
    print("Inputs are vaildated")
