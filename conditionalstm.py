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

# year = input("enter year: ")
# daysInTheYear = int(input("How many days are there in this year: "))

# if daysInTheYear == 365:
#     print(f"{year} is Not a Leap year")
# elif daysInTheYear == 366:
#     print(f"{year} is a Leap year")
# else:
#     print("")


userAGe = int(input("Plese, your age: "))
userNationality = input("What Country are you from?: ")
havePvc = (input("Do you have PVC?: "))

if userAGe >= 18:
    if userNationality == "Nigerian":
        if havePvc == "Yes" or havePvc == "YES" or havePvc == "yes":
            print("WELCOME!!!: You are eligible for voting")
        else:
            print("NO PVC, NO VOTING. GO HOME!!")
    else:
        print("You annot vote, Go to your country!!")
else:
    print("You are not up to the age")