prices = [7,6,4,3,1]
def foo(prices):
    max_profit = 0
    current_price = prices[0]
    for next_price in prices[1:]:
        if next_price > current_price:
            profit = next_price - current_price
            max_profit = max(max_profit, profit)
        else:
            current_price = next_price
    return max_profit

if __name__ == "__main__":
    max_profit = foo(prices)
    print(max_profit)
    