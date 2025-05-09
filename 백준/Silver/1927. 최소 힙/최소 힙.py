import sys
import heapq

n = int(sys.stdin.readline())
heap = []

for i in range(n) :
  x = int(sys.stdin.readline())
  if x > 0 :
    heapq.heappush(heap, x)
  elif x == 0 :
    if len(heap) == 0 :
      print(0)
    else :
      print(heapq.heappop(heap))
    