num = input()
nums = [int(num) for num in input()]
sum = 0

for i in range(len(nums)) :
  sum += nums[i]
  
print(sum)   