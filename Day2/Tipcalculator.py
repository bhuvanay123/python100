print("Welcome to the tip calculator")
tot_bill = float(input("what was the total bill?"))
tip = int(input("what percentage of tip would u like to give?10,12 or 15?"))
people = int(input("How many people to split the bill?"))
tip_amt = tot_bill * (tip / 100)
tot_bill_w_tip = tot_bill + tip_amt
each_person_pay = tot_bill_w_tip / people
each_person_pay = "{:.2f}".format(each_person_pay)
print(f"Each person should pay: ${each_person_pay}")