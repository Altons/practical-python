# report.py
#
# Exercise 2.4

import csv


def read_portfolio(filename):
    try:
        f = open(filename, 'rt')
        rows = csv.reader(f)
        headers = next(rows)
        portfolio = []

        for row in rows:
            symbol = (row[0], int(row[1]), float(row[2]))
            portfolio.append(symbol)
    except:
        print("Can't read file", filename)
    return portfolio


def read_prices(filename):
    try:
        f = open(filename, 'rt')
        rows = csv.reader(f)
        prices = []
        for row in rows:
            if len(row) > 0:
                price = (row[0], float(row[1]))
                prices.append(price)
    except:
        print("Can't read price file", filename)
    return prices


def make_report(portfolio, prices):
    report = []
    for price in prices:
        print(price)
        for share in portfolio:
            print(share)
            if price[0] == share[0]:
                print(price[0])
                change = share[2] - price[1]
                report.append((share[0], share[1], share[2], change))
    return report
