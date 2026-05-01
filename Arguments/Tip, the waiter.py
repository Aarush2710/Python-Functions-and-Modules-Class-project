def calculte(bill_amount, tip_amount):

    if bill_amount <=0:

        print("Bill amount must be greater than zero.")

    else:

        tip_perc = (tip_amount/bill_amount) * 100

    return tip_perc

tip = calculte(1520, 100)

print("The tip percentage is : ", tip)