import sys

def snail2() :
  a, b, v = [int(x) for x in sys.stdin.readline().split()]

  everyday  = a - b # 하루높이
  real_v = v - b # 미끄러지는거 고려안함
  
  day = real_v // everyday
  
  if real_v % everyday != 0 :
    day += 1
  print(day)
  
snail2()