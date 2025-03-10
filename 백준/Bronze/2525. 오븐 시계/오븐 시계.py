import sys

hour, minute = [int(i) for i in sys.stdin.readline().split()]
cook_minute = int(sys.stdin.readline())

def get_cook_time(hour, minute, cook_minute) :
  minute += cook_minute
  
  if minute >= 60 :
    hour += minute // 60
    minute = minute % 60
  if hour >= 24 :
    hour = hour % 24
  print(hour, minute)
  
get_cook_time(hour, minute, cook_minute)