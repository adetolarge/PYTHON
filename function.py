def hello():
    print('Hello World')
def greetings():
    age = 50
    name = "Adetola"
    print(f'Hello {name} How are you? In 5 years time, you will be {age+5} years old. ')

#create a funtion that calculates the square root of a number
def cube(number):
    return number ** 3
num = int(input("Please enter a number: "))
result = cube(num)
print(f"The cube of {num} is {result}")
#Assignment
#Write a Python function that prompts the user to enter a number. Then, given that number, it prints the sentence "Hello, Python!" that many times.
def random_number():
    number_input = int(input("Please enter a number: "))
    for i in range(number_input):
        print(f"Hello, {i} Python!")
random_number()

