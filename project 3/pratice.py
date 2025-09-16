print("Welcome to Rollercoaster!")
height = int(input("Enter your height in cm: "))
age = int(input("Enter your age: "))
bill = 0

if height >= 120:
    print("Yes you can ride rollercoaster")
    if age <= 12 :
        bill = 5
        print("Please Pay $5")
    elif age <= 18:
        bill = 7
        print("please Pay $7")
    elif age >=45 and age<=55:
        print("Everything will be ok, have a free ride on us!")
    else:
        bill = 12
        print("Please Pay $12")
    want_photo = input("Do you want a photo taken ? Y or N. ")
    if want_photo == 'y':
        bill += 3
    print(f"Your final bill is ${bill}")
else:
    print("You can't ride rollercoaster")



# number = int(input("Which number do you want to check? "))

# if number%2 == 0:
#     print("even")
# else:
#     print("odd")