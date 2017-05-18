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
print("\nTHE END.")
