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

print(f"Remaining balance: {balance:.2f}") #formating the result to 2 decimals

"""
Task 2:

Paying debt off in a year; finding the minimum fixed payment rate 
with a given annual interest rate

"""

annual_interest_rate = 0.2
payment_months = 12
increment = 10 # monthly payment should be a multiple of 10
paid = False # setting this as False, as in the beginning debt is not paid

for num_increments in range(1, 100000): # we guess a range for multiples of 10 that should cover the right min payment
    balance = 3926
    fixed_monthly_payment = num_increments * increment # making sure that payment is a multiple of 10
    for month in range(1, payment_months + 1):  # adding 1 to include the 12th month
        remaining = balance - fixed_monthly_payment
        balance = remaining + (remaining*(annual_interest_rate/12))
        if balance <= 0: # if balance is less than 0 we have managed to pay the debt and can break the loop
            paid = True
            break
    if paid is True:
        print("Lowest payment: ", fixed_monthly_payment)
        break
if paid is False: # making sure that we know when the payments weren't enough to pay the debt
    print("Debt not paid!")


"""
Task 3:

Using bisection search to find out the exact minimum fixed monthly payment more efficiently to pay off the debt in one year

"""

import time

t1 = time.time()

initial_balance = 999999
annual_interest_rate = 0.18
monthly_interest_rate = annual_interest_rate / 12
payment_months = 12

# setting the lower and upper bound for the search
low = initial_balance / 12
high = (initial_balance * (1 + monthly_interest_rate)**12) / 12

paid = False 

while paid is False: # the loop continues until paid is defined True
    balance = initial_balance  # defining the balance at the beginning so that the balance is always the same in the beginning of the loop 
    fixed_monthly_payment = (high+low)/2
    for month in range(1, payment_months + 1):  # adding 1 to include the 12th month
        remaining = balance - fixed_monthly_payment
        balance = remaining + (remaining*monthly_interest_rate)
        if abs(balance) < 0.01: # finding the fixed payment with one cent accuracy; loop break when this happens
            paid = True
            print(f"Lowest payment: {fixed_monthly_payment:.2f}")
            break
    if balance > 0.01:
        low = fixed_monthly_payment
    else: 
        high = fixed_monthly_payment

t2 = time.time()

print(f"Time in seconds: {t2-t1:.4f}")