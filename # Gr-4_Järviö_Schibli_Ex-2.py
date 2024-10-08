# Gr-4_Järviö_Schibli_Ex-2

balance = 42
annual_interest_rate = 0.2
monthly_payment_rate = 0.04
payment_months = 12

for i in range(0,payment_months + 1):
    if i == 0:
        min_payment = balance * monthly_payment_rate
        remaining = balance - min_payment
        balance_new = remaining + (remaining*(annual_interest_rate/12))
        print("Month", i, "remaining balance: ", balance)
    elif i == 1:
        min_payment = balance * monthly_payment_rate
        remaining = balance - min_payment
        balance_new = remaining + (remaining*(annual_interest_rate/12))
        print("Month", i, "remaining balance: ", format(balance_new, '.2f'))
    else:
        min_payment = balance_new * monthly_payment_rate
        remaining = balance_new - min_payment
        balance_new = remaining + (remaining*(annual_interest_rate/12))
        print("Month", i, "remaining balance: ", format(balance_new, '.2f'))



