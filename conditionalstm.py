# studentAge = int(input("What Is Your Age?: "))

# if studentAge<15:
#     print("You Wish😂😂😂")
# elif studentAge<20:
#     print("You are not even a man yet")
# else:
#     print("Wait small")



# if input("Start the Conversation:" ) == "Hello":
#     print("Hello How are you")
# else:
#     print("")

year = input("enter year: ")
daysInTheYear = int(input("How many days are there in this year: "))

if daysInTheYear == 365:
    print(f"{year} is Not a Leap year")
elif daysInTheYear == 366:
    print(f"{year} is a Leap year")
else:
    print("")