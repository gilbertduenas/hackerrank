# https://www.hackerrank.com/challenges/calendar-module/problem

import calendar

M, D, Y = map(int, input().split())
print(calendar.day_name[calendar.weekday(Y, M, D)].upper())
