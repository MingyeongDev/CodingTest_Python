array = []

for _ in range(9) :
    num = int(input())
    array.append(num)

print(max(array))
print(array.index(max(array)) + 1)