import random


def pass_gen(count_char=8):
    dict_values = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                   'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                   's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '.',
                   'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
                   'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                   'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0',
                   '1', '2', '3', '4', '5', '6', '7', '8', '9']
    passw = []
    for i in range(count_char):
        passw.append(random.choice(dict_values))
    return "".join(passw)

while True:
    print("Count chars for password(exit = 0):", end=" ")
    count = int(input())
    if count == 0:
        break
    print(pass_gen(count))
print()
print("THE END")
