import sys

n, m = [int(i) for i in sys.stdin.readline().split()]
money = [int(i) for i in sys.stdin.readline().split()]

window = sum(money[:m])
result = window
for i in range(m, n) :
  window += money[i] - money[i - m]
  result = max(result, window)
print(result)