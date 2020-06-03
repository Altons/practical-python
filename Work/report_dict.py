
def read_portfolio(filename):
    try:
        f = open(filename, 'rt')
        rows = csv.reader(f)
        headers = next(rows)
        portfolio = []

        for row in rows:
            symbol = {headers[0]: row[0], headers[1]: int(row[1]), headers[2]: float(row[2])}
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
                price = {'name': row[0], 'price': float(row[1])}
                prices.append(price)
    except:
        print("Can't read price file", filename)
    return prices


def make_report(portfolio, prices):
    for price in prices:
        for share in portfolio:
            if price['name'] == share['name']:
                share['change'] = share['price'] - price['price']
    return portfolio
