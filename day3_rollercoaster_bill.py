print("Welcome to the rollercoaster!")
height = int(input("what is your height in cm?\n"))

if height > 120:
    print("You can ride the rollercoaster!")
    Age = int(input("What is your age?\n"))
    if Age < 12:
        bill = 5
        print("Child ticket is $5.")
    elif Age <= 18:
        bill = 7
        print("Youth ticket is $7")
    elif Age >= 45 and Age <= 55:
        bill = 0
        print("Everything is going to be okay! Have a free ride on us!")
    else:
        bill = 12
        print("Adult ticket is $12.")
        
    wants_photo = input("Do you want a photo taken? Y or N?")
    if wants_photo == "Y":
        bill += 3
        print(f"Your bill is {bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")
    