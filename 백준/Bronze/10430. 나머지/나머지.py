import sys
a, b, c = [int(i) for i in sys.stdin.readline().split()]
print((a + b) % c)
print(((a % c) + (b % c)) % c)
print((a * b) % c)
print(((a % c) * (b % c)) % c)