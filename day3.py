height = int(input("What is your height in cm?"))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12")
else:
    print("Sorry, you have to grow taller before you can ride")

number = int(input("Which number do you want to change"))

if number % 2 == 0:
    print("this is an even number")
    
else:
    print("this is a odd number")


