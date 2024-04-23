from itertools import product

k, M = map(int, input().split())
integers = list(map(int, input().split()[1:]) for _ in range(k))

values = product(*integers)

max_profit = 0
for val in values:
    max_profit = max(max_profit, sum(map(lambda x: x**2, val)) % M)

print(max_profit)
