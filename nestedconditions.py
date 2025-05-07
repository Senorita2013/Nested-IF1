

#exam elligibility check
medical_cause=input("Do you have a medical cause Y or N:")
atten=int(input("Enter the attendance of the student:"))

if medical_cause == "Y":
    print("You are allowed as a medical cause")
else:
    if atten >= 75:
        print("Allowed as attendance is more than 75")
    else:
        print("Not allowed")

#electricity bill
units=int(input("Enter the number of units cosumed:"))

if(units<50):
    amount=units*2.60
    tax=25
elif (units<=100):
    amount=units*3.25
    tax=35
elif (units<=200):
    amount=units*5.26
    tax=45

else:
    amount=units*8.45
    tax=75

total=amount+tax
print("The electricity bill is",total)

#select your choice of ride
print("Select your ride:")
print("1. Bike")
print("2. Car")

choice=int(input("Enter your choice:"))

if choice==1:
    print("What type of bike?")
    print("1. Scooty")
    print("2. Scooter")
    choice2=int(input("Enter your choice of bike"))
    if choice2==1:
        print("You have selected scooty")
    else:
        print("You have selected scooter")

elif choice==2:
    print("What type of car?")
    print("1. Sedan")
    print("2. XUV")
    choice3=int(input("Enter your choice of car"))
    if choice3==1:
        print("You have selected Sedan")
    else:
        print("You have selected XUV")
else:
    print("Wrong choice!")