principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment = 1000
month = 1
extra_payment_start_month = 60
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    if extra_payment_start_month <= month <= extra_payment_end_month:
        special_payment = payment + extra_payment
    else:
        special_payment = payment
    if special_payment > principal:
        special_payment = principal * (1+rate/12)
    principal = principal * (1+rate/12) - special_payment
    total_paid = total_paid + special_payment
    print(month, total_paid, round(principal, 2))
    month += 1

print('Total paid', total_paid)
print('Total month', month-1)
