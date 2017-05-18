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
print("\nTHE END.")