# pcost.py
#
# Exercise 1.27
import csv


def portfolio_cost(filename):
    f = open(filename, "rt")
    rows = csv.reader(f)
    headers = next(rows)
    total = 0.0
    for rowno, row in enumerate(rows):
        try:
            record = dict(zip(headers, row))
            shares = int(record['shares'])
            price = float(record['price'])
            total += shares*price
        except ValueError:
            print(f'Row {rowno}: Bad row: {row}')
    f.close()
    return total
