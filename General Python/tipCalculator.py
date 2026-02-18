#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number.

print("Welcome to the tip calculator!")
bill = input("What was the total bill? $")
tip = input("How much tip would you like to give? ")
people = input("How many people to split the bill? ")
bill_as_float = float(bill)
tip_as_int = int(tip)
people_as_int = int(people)
tip_as_percent = tip_as_int / 100
total_tip_amount = bill_as_float * tip_as_percent
total_bill = bill_as_float + total_tip_amount
bill_per_person = total_bill / people_as_int
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")
# print(f"Each person should pay: ${final_amount}")
