#4
def is_palindrome(s):
    return s == s[::-1]


def check_almost_palindrome(s):
    for i in range(len(s)):
        candidate = s[:i] + s[i + 1:]
        if is_palindrome(candidate):
            return f"არ არის პალინდრომი, მაგრამ თუ მოინდომებ და ამოიღებ '{s[i]}' პოზიციაზე {i}-ზე, გამოვა პალინდრომი: '{candidate}'"

    for i in range(len(s) + 1):
        for ch in 'abcdefghijklmnopqrstuvwxyz0123456789':
            candidate = s[:i] + ch + s[i:]
            if is_palindrome(candidate):
                return f"არაა პალინდრომი, მაგრამ მოინდომე და თუ ჩასვამ '{ch}' პოზიციაზე {i}-ზე, გამოვა პალინდრომი: '{candidate}'"

    return "არ არის პალინდრომი და ვერ გააპალინდრომებ."


def main():
    user_input = input("შეიყვანე ტექსტი (მხოლოდ ასოები ან ციფრები): ").lower()

    # ამოწმებს შეიცავს თუ არა მხოლოდ ასოებს ან ციფრებს
    if not user_input.isalnum():
        print("შეიყვანე მხოლოდ ასოები ან ციფრები თუ გინდა გინდა.")
        return

    if is_palindrome(user_input):
        print("ეს ტექსტი პალინდრომია ")
    else:
        result = check_almost_palindrome(user_input)
        print(result)


main()

#5
def generate_nicknames(word):
    nicknames = [
       word + "_1996",
       word + "_ვოლკი",
       word + "_store",
       word + "aq_yvelaferia",
       word + "dzmas_venacvale"
    ]
    return nicknames
def main():
    user_input = input("შეიყვანე მხოლოდ ერთი სიტყვა: ").strip()
    if not user_input.isalnum():
        print("წაკითხულის გააზრება გიჭირთ")
        return
    nicknames = generate_nicknames(user_input.lower())
    print("\nშენი ზედმეტსახელები:")
    for name in nicknames:
        print(" ", name)

main()

#6

import random

def get_valid_numbers():
    while True:
        user_input = input("შეიყვანე რიცხვები გამოტოვებით გამოყოფილი (მაგ: 1 2 3 ): ")

        items = user_input.strip().split()


        if all(item.isdigit() or (item.startswith('-') and item[1:].isdigit()) for item in items):

            return [int(num) for num in items]
        else:
            print("მხოლოდ მთელი რიცხვები არის დაშვებული! სცადე თავიდან.\n")

def main():
    numbers = get_valid_numbers()

    print("\nაირჩიე როგორ გინდა რომ დავალაგო მონაცემები:")
    print("1 - ზრდადობით")
    print("2 - კლებადობით")
    print("3 - შემთხვევითად (random)")
    print("4 - მხოლოდ უნიკალური მონაცემები")

    choice = input("შეიყვანე შესაბამისი ნომერი (1/2/3/4): ").strip()

    if choice == "1":
        sorted_list = sorted(numbers)
        print("\nდალაგებული ზრდადობით:", sorted_list)

    elif choice == "2":
        sorted_list = sorted(numbers, reverse=True)
        print("\nდალაგებული კლებადობით:", sorted_list)

    elif choice == "3":
        shuffled = numbers.copy()
        random.shuffle(shuffled)
        print("\nშემთხვევითი რიგითობით:", shuffled)

    elif choice == "4":
        unique = list(set(numbers))
        print("\nმხოლოდ უნიკალური ელემენტები:", unique)

    else:
        print("უნდა შეგეყვანა მხოლოდ 1 2 3 ან 4, ახლა გვიანია.")


main()