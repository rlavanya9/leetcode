def maxProfit(prices):
        asc_list = sorted(prices)
        desc_list = sorted(prices, reverse=True)
        if asc_list == prices:
            profit = prices[len(prices)-1] - prices[0]
            return profit
        elif desc_list == prices:
            profit = 0
            return profit
        else: 
            # prev_price = -1
            prev_price = None
            profit = 0
            for price in prices:
                # if price > prev_price and prev_price != -1:
                if price > prev_price and prev_price != None:
                    profit = profit + (price - prev_price)
                prev_price = price
            return profit

print(maxProfit([1,2,3,4,5]))
print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))
print(maxProfit([2,1,2,0,1]))

        