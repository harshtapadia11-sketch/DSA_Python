prices = [7,6,4,3,1]
# maxprofit=0
# for i in range(len(prices)):
#     for j in range(i+1,len(prices)):
#         if prices[j]-prices[i]>maxprofit:
#             maxprofit=prices[j]-prices[i]

min_price = prices[0]
max_profit = 0

for i in range(len(prices)):

    if prices[i] < min_price:
        min_price = prices[i]

    profit = prices[i] - min_price

    if profit > max_profit:
        max_profit = profit

print(max_profit)

        