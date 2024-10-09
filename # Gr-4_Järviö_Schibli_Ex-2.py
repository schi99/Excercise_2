# Gr-4_Järviö_Schibli_Ex-2
"""
Task 1:

Calculating the credit card balance after one year with minimum monthly payments 
with the given annual and monthly payment rates and 12 months of payments
"""
balance = 484
annual_interest_rate = 0.2
monthly_payment_rate = 0.04
payment_months = 12

for month in range(1, payment_months + 1):  #adding 1 to include the 12th month
        min_payment = balance * monthly_payment_rate
        remaining = balance - min_payment
        balance = remaining + (remaining*(annual_interest_rate/12))

print("Remaining balance: ", format(balance, '.2f')) #formating the result to 2 decimals

"""
Task 2:

Paying debt off in a year; finding the minimum fixed payment rate 
with a given annual interest rate

"""

balance = 484
annual_interest_rate = 0.2
payment_months = 12

monthly_payment = 0 



