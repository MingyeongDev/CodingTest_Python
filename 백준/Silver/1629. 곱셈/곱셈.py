import sys
a, b, c = [int(x) for x in sys.stdin.readline().split()]

def code(a, b, c) :
  if b == 1 :
    return a % c
  else :
    abc = code(a, b // 2, c)
    if b % 2 == 0 :
      return abc * abc % c
    else :
      return abc * abc * a % c
  
print(code(a,b,c))