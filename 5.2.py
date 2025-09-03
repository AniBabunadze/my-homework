
#8
from datetime import datetime, timedelta
import random

start = datetime.now()
player1_finish = start + timedelta(seconds=random.randint(5, 20))
player2_finish = start + timedelta(seconds=random.randint(5, 20))

player1_time = (player1_finish - start).total_seconds()
player2_time = (player2_finish - start).total_seconds()

print(f" 1 დაასრულა {player1_time} წამში.")
print(f" 2 დაასრულა {player2_time} წამში.")

if player1_time < player2_time:
    print("გაიმარჯვა 1")
elif player2_time < player1_time:
    print("გაიმარჯვა 2")
else:
    print("ფრე")


#9

from datetime import date, datetime

bd = input(" დაბ.დღე :(YYYY-MM-DD): ")
b = datetime.strptime(bd, "%Y-%m-%d").date()
t = date.today()
n = b.replace(year=t.year)
if n < t:
    n = n.replace(year=t.year + 1)
print(f"დარჩენილია {(n - t).days} დღე შემდეგ დაბადების დღემდე.")

#10
import random
import itertools

all_combinations = list(itertools.product(range(1, 7), repeat=4))
day = 1
while True:
    password = [random.randint(1, 6) for _ in range(4)]
    print(f"\n დღე {day} — პაროლი გენერირებულია.")
    for attempt in all_combinations:
        print(f"დღე {day} | ვცდილობთ: {attempt}")
        if list(attempt) == password:
            print(f"\n პაროლი სწორია: {attempt} — საცავი გახსნილია {day} დღეში!\n")
            exit()

        day += 1
