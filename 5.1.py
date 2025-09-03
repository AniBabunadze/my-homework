#1
from itertools import permutations

word = "ABCD"
count = len(list(permutations(word, len(word))))
print(count)




#2
from datetime import date , timedelta

today = date.today()
next_tuesday = today + timedelta((1 - today.weekday()) % 7 or 7)
print(next_tuesday)

#3
user = int(input("enter year: "))
if user % 4 == 0 and user % 100 != 0 or user % 400 == 0:
    print("ნაკიანია")
else :
    print("არ არის ნაკიანი")

import calendar
year = int(input("enter year: "))
if calendar.isleap(year):
    print(f'{year} ნაკიანია')
else:
    print(f"{year} არ არის ნაკიანი")

#4
from datetime import date
today = date.today()
new_year = date(today.year + 1, 1, 1)
weeks_left = (new_year - today).days // 7
print(weeks_left)

#5
from itertools import combinations
my_list =[1,2,3,4,5]
print(list(combinations(my_list, 2)))

#6
import itertools

chars = ['X', 'Y', 'Z']
for r in range(1, 4):
    for combo in itertools.product(chars, repeat=r):
        print(''.join(combo))


