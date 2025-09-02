#7

import re

def clean_text(text):
    cleaned = re.sub(r'[^a-zA-Zა-ჰ\s]', '', text)
    return cleaned

text = input("შეიყვანე ტექსტი: ")
result = clean_text(text)

print("გაწმენდილი ტექსტი:", result)

#8
def build_pyramid(numbers):
    pyramid = [numbers]

    while len(pyramid[0]) > 1:
        prev_row = pyramid[0]
        new_row = [prev_row[i] + prev_row[i + 1] for i in range(len(prev_row) - 1)]
        pyramid.insert(0, new_row)

    return pyramid

def print_pyramid(pyramid):
    max_width = len("   ".join(map(str, pyramid[-1])))
    for row in pyramid:
        line = "   ".join(map(str, row))
        print(line.center(max_width))

input_str = input("შეიყვანეთ რიცხვები მძიმის გამოყენებით (მაგ. 3,5,7,2): ")
numbers = [int(x.strip()) for x in input_str.split(",")]

pyramid = build_pyramid(numbers)
print("\nპირამიდა:\n")
print_pyramid(pyramid)


#9

import re
from collections import Counter

text = input("შეიყვანე ტექსტი: ").lower()
words = re.findall(r'\b\w+\b', text)
counts = Counter(words)
max_count = max(counts.values())
most_common = [w for w, c in counts.items() if c == max_count]

print(f"ყველაზე ხშირი სიტყვაა და გამეორდა ({max_count}-ჯერ): {', '.join(most_common)}")



#10

def words_length_dict(sentence):
    words = sentence.split()
    return {word: len(word) for word in words}

user_input = input("შეიყვანე წინადადება: ")
result = words_length_dict(user_input)

print(result)