

def finalPrices(prices):
    finalPrices = []
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[j] <= prices[i]:
                finalPrices.append(prices[i] - prices[j])
                break
            else:
                if j == len(prices) - 1:
                    finalPrices.append(prices[i])
    finalPrices.append(prices[i])
    return finalPrices








prices = [10,1,1,6]
print(finalPrices(prices))