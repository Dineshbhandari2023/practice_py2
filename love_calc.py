import random

print ("Welcome to love calculator!")

your_name = input("What is your name?")
their_name = input("What is their name?")

combined_string = your_name + their_name
lower_case = combined_string.lower()

t = lower_case.count("t")
r = lower_case.count("r")
u = lower_case.count("u")
e = lower_case.count("e")

true = t + r + u + e

l = lower_case.count("l")
o = lower_case.count("o")
v = lower_case.count("v")
e = lower_case.count("e")

love = l + o + v + e

love_score = int (str(true) + str(love)).randint(1,100)
print (love_score)

if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score > 40) and (love_score < 50):
    print(f"your score is {love_score}, you are alright together.")
else:
    print(f"your score is {love_score}.")  