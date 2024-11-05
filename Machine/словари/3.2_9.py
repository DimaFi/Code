n = int(input())
accounts = {}

for _ in range(n):
    line = input().strip()
    name, amount = line.split(',')
    amount = int(amount)
    
    money = amount
    commission = amount
    
    if name in accounts:
        accounts[name][0] += money
        accounts[name][1] += commission
    else:
        accounts[name] = [money, commission]

sorted_accounts = sorted(
    accounts.items(),
    key=lambda x: (-x[1][0], x[0])
)

for name, (money, commission) in sorted_accounts:
    print(f"{name} {money*0.95:.2f} {commission*0.05:.2f}")
