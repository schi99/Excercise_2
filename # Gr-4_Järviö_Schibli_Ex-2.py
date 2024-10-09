# Gr-4_Järviö_Schibli_Ex-2
"""
Calculating the credit card balance after one year with minimum monthly payments 
with the given annual and monthly payment rates and 12 months of payments
"""
balance = 484
annual_interest_rate = 0.2
monthly_payment_rate = 0.04
payment_months = 12

for i in range(1, payment_months + 1):  #adding 1 to include the 12th month
    if i == 1: # because of the variable names the code for the first month is different
        min_payment = balance * monthly_payment_rate
        remaining = balance - min_payment
        balance_new = remaining + (remaining*(annual_interest_rate/12))
    else:
        min_payment = balance_new * monthly_payment_rate
        remaining = balance_new - min_payment
        balance_new = remaining + (remaining*(annual_interest_rate/12))

print("Remaining balance: ", format(balance_new, '.2f')) #formating the result to 2 decimals



