# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment = 1000
month = 1
while principal > 0:
    if month <= 12:
        special_payment = payment + extra_payment
    else:
        special_payment = payment
    principal = principal * (1+rate/12) - special_payment
    total_paid = total_paid + special_payment
    month += 1

print('Total paid', total_paid)
print('Total month', month-1)
