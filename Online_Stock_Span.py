# Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day.

# The span of the stock's price in one day is the maximum number of consecutive days (starting from that day and going backward) for which the stock price was less than or equal to the price of that day.

# For example, if the prices of the stock in the last four days is [7,2,1,2] and the price of the stock today is 2, then the span of today is 4 because starting from today, the price of the stock was less than or equal 2 for 4 consecutive days.
# Also, if the prices of the stock in the last four days is [7,34,1,2] and the price of the stock today is 8, then the span of today is 3 because starting from today, the price of the stock was less than or equal 8 for 3 consecutive days.
# Implement the StockSpanner class:

# StockSpanner() Initializes the object of the class.
# int next(int price) Returns the span of the stock's price given that today's price is price.

# Constraints:

# 1 <= price <= 105
# At most 104 calls will be made to next.


# Key idea: use monotonic stack - 
# for each new price, we want to know how many consecutive days previously has a price <= curr_price
# instead of scanning through each price backwards, keep a stack of pairs (price, span)
# the stack is kept in decreasing price order

# when a new price comes in:
# 1) starts with span = 1
# 2) while the top of the stack has price <= curr_price, pop it and adds its span
# 3) push (curr_price, span)
# 4) return span
# This makes each price gets pushed and poped at most once, so next() is amortized O(1)
class StockSpanner:

    def __init__(self):
        # stack stores pairs
        self.stack = [] # Python lists are dynamic and can store any type of elements

    def next(self, price: int) -> int:
        span = 1

        # merge all previous prices that are <= curr_price
        # self.stack is a list of tuples - each element stores price and span
        # price is the stock price on that day; span is how many consecutive days that price already covered
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1] # extract the span

        self.stack.append((price, span))
        return span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

# Time: O(1) a single call can pop many items, but each pair (price, span) is pushed and poped at most once - so across all call, total work is linear
# Space: O(n) the stack can grow up to n, where n is the number of call


