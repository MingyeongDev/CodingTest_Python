basket_count, change_count = [int(i) for i in input().split()]

baskets = [i + 1 for i in range(basket_count)]

for i in range(change_count) :
  start, end = [int(i)-1 for i in input().split()]
  baskets[start], baskets[end] = baskets[end], baskets[start]

print(*baskets)