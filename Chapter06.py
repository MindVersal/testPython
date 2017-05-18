print("Chapter 06.\n")
for x in range(-10, 10):
    print("Test %s" % x)
print("\nList Range:")
print(list(range(0, 10)))
print("\nInput number")
number = input("Number is: ")
if bool(number.strip()):
    print("Your answer is %s" % number)
elif not bool(number.strip()):
    print("Sorry, but your answer is wrong...")
print('\nTest File:')
test_file = open('./test.txt')
text = test_file.read()
print(text)
print('\nTest sum')
test_a = abs(10) + -10
print(test_a)
print('Crypt word:')
test_word = "aaa bbb ccc ddd eee fff ggg hhh iii jjj kkk lll mmm ooo ppp qqq rrr sss ttt uuu vvv www xxx yyy zzz"
split_word = test_word.split(" ")
for i in range(0, len(split_word), 2):
    print(split_word[i])
print("\nTHE END.")
