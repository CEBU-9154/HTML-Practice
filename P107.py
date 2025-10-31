def count_ways(coins, n, amount):
    if amount==0:
        return 1
    if amount<0:
        return 0
    if n==0 and amount > 0:
        return 0
    
    return count_ways(coins, n, amount - coins[n-1]) + count_ways(coins, n-1, amount)
coins=[1,2,3]
amount=int(input("Enter total amount: "))
n=len(coins)

print(f"\nNumber of ways to divide ${amount} using coins {coins} is: ", count_ways(coins,n,amount))