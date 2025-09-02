#1
import random
import string

def generate_password():
    try:
        length = int(input("შეიყვანე პაროლის სიგრძე: "))
    except ValueError:
        print("შეიყვანე რიცხვი პაროლის სიგრძისთვის!")
        return

    include_lowercase = input("გსურს პატარა ლათინური ასოები? (y/n): ").lower() == 'y'
    include_uppercase = input("გსურს დიდი ლათინური ასოები? (y/n): ").lower() == 'y'
    include_digits = input("გსურს ციფრები? (y/n): ").lower() == 'y'
    include_symbols = input("გსურს სიმბოლოები? (y/n): ").lower() == 'y'

    characters = ""
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation


    if not characters:
        print("უნდა აირჩიო მინიმუმ ერთი სიმბოლოთა ჯგუფი (ასოები, რიცხვები ან სიმბოლოები).")
        return
    password = ''.join(random.choice(characters) for _ in range(length))
    print(f"შენი პაროლია: {password}")

generate_password()


#2
import re

def evaluate_password_strength(password):
    score = 0


    length = len(password)
    if length >= 12:
        score += 3
    elif length >= 8:
        score += 2
    elif length >= 6:
        score += 1


    digits = len(re.findall(r'\d', password))
    if digits >= 2:
        score += 2
    elif digits == 1:
        score += 1


    specials = len(re.findall(r'[!@#$%^&*(),.?":{}|<>]', password))
    if specials >= 2:
        score += 2
    elif specials == 1:
        score += 1


    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    if has_upper and has_lower:
        score += 2


    if re.search(r'(.)\1\1', password):
        score -= 1


    if score <= 3:
        strength = "weak"
    elif score <= 6:
        strength = "medium"
    else:
        strength = "strong"

    return score, strength


password = input("შეიყვანე პაროლი: ")
score, strength = evaluate_password_strength(password)
print(f"შეფასება: {score}/10 – {strength}")

#3

def fib_sequence():
    while True:
        user_input = input("გთხოვ შეიყვანე რიცხვი (ფიბონაჩის სიგრძე): ")

        if user_input.isdigit():
            n = int(user_input)
            if n <= 0:
                print("გთხოვ შეიყვანე დადებითი რიცხვი!")
                continue
            break
        else:
            if user_input.isalpha():
                print(f"შენ შემოიტანე ტექსტი: '{user_input}', არასწორია — მხოლოდ რიცხვი!")
            elif any(not c.isdigit() for c in user_input):
                print(f"შენ შემოიტანე სიმბოლო ან არასწორი ფორმატი: '{user_input}', მხოლოდ რიცხვი შეიყვანე!")
            else:
                print("არასწორი შეყვანა — გთხოვ შეიყვანე მხოლოდ რიცხვი!")


    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])

    print(f"ფიბონაჩის რიგი ({n} ელემენტი): {fib[:n]}")
fib_sequence()
