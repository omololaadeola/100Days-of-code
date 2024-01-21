print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
combine_name = name1 + name2
lowername = combine_name.lower()
t = lowername.count("t")
r = lowername.count("r")
u = lowername.count("u")
e = lowername.count("e")
first = t + r + u + e

l = lowername.count("l")
o = lowername.count("o")
v = lowername.count("v")
e = lowername.count("e")
second = l + o + v + e

love_score = int(str(first) + str(second))
if love_score < 10 or love_score > 90:
  print(f"Your score is {love_score}, you go together like coke and fanta.")
elif love_score > 40 and love_score < 50:
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")
  