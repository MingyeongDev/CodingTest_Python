hour, minute = map(int, input().split())
timer = int(input())

def get_cook_time(hour, minute, timer) :
  minute += timer
  
  if minute >= 60 :
    hour += minute // 60
    minute = minute % 60
  if hour >= 24 :
    hour = hour % 24
  print(hour, minute)
  
get_cook_time(hour, minute, timer)