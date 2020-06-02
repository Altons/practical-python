# pcost.py
#
# Exercise 1.27

import csv


def portfolio_cost(filename):
    try:
        f = open(filename, "rt")
        rows = csv.reader(f)
        next(rows)
        total = 0
        for row in rows:
            total += int(row[1])*float(row[2])
        f.close()
        return total
    except Exception:
        print("Couldn't parse", Exception)
