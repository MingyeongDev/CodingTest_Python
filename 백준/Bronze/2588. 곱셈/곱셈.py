first = int(input())
second = int(input())

print(first * (second % 10))
print(first * ((second // 10) % 10))
print(first * (second // 100))
print(first * second)