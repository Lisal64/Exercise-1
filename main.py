# Exercise 1

def name_age():
    name = str.capitalize(input("Please enter your name: "))
    age = input("Please enter your age: ")  # is automatically a string, doesn't need conversion
    print(f"Hello {name.upper()}. Your age is: {age}")
    # name.upper added only here, so that it doesn't interfere with the return
    return (name + age)  # using + to create a concatenated string to be returned


print(name_age())

# Exercise 2

num1 = int  # defining variables as integers
num2 = int



# defining the function:
def swap_integers(num1, num2):
    num1 = int(input("Please enter the value of x: "))  # to classify both numbers as integers
    num2 = int(input("Please enter the value of y: "))
    num3 = num1
    num1 = num2
    num2 = num3
    print(f"After swap:\nX={num1}\nY={num2}\n")
    num1_as_string = str(num1)  # to make sure the return is a concatenated string
    num2_as_string = str(num2)
    print("Return value: ", end="")
    # using end to eliminate the line break that would be added automatically
    return (num1_as_string + num2_as_string)


print(swap_integers(num1, num2))


# Exercise 3

def check_numbers(num1, num2):
    num1 = int(input("Please enter the value of x: "))
    num2 = int(input("Please enter the value of y: "))
    if num1 % 6 == 0 or num2 % 6 == 0:  # to make sure this is true the "rest" remaining from the division needs to be 0
        print("One number is divisible by 6.")
    else:
        print("No numbers are divisible by 6.")
    if num1 % 10 == 0 and num2 % 10 == 0:
        print("Both numbers are divisible by 10.")
    else:
        print("Both numbers are not divisible by 10.")
    if (num1 % 6 == 0 or num2 % 6 == 0) and (num1 % 10 == 0 and num2 % 10 == 0):
        print("Return value: ", end="")
        return ("True")
    else:
        print("Return value: ", end="")
        return ("False")


print(check_numbers(num1, num2))


# Exercise 4

def sum_up(num1, num2):
    num1 = int(input("Please enter the value of x: "))
    num2 = int(input("Please enter the value of y: "))
    if num2 > num1 and num1 > 0 and num2 > 0:
        # all of these need to be true in order to continue, so we can put it in one if-clause
        inclusive_sum = int(
            sum(range(num1, num2 + 1)))  # +1 because the last number needs to be included in the range as well
        return (inclusive_sum)
    else:
        return (0)


print(sum_up(num1, num2))

# Exercise 5

r1 = float
r2 = float
r3 = float


def circle_area(r1, r2, r3):
    r1 = float(input("Please enter the first circle radius: "))
    r2 = float(input("Please enter the second circle radius: "))
    r3 = float(input("Please enter the third circle radius: "))
    pi = float(3.14)  # defining pi with the first 3 letters
    return (float(pi * r1 ** 2 + pi * r2 ** 2 + pi * r3 ** 2))  # calculating the 3 circle areas and adding them


print(circle_area(r1, r2, r3))

# Exercise 6

text = str


def check_string(text):
    text = str(input("Please enter a text: "))
    if text.startswith("a") or text.endswith("a"):
        return ("True")
    elif text.startswith("A") or text.endswith("A"):  # to take capitalized letters into account
        return ("True")
    else:
        return ("False")


print(check_string(text))

# Exercise 7

rows = int


def triangle(rows):
    rows = int(input("Please enter the number of rows you want your triangle to have: "))
    for row in range(rows):
        # adding a loop to print the stars for the number of rows, don't need to specify 0 starts there automatically
        for column in range(row + 1):  # second loop to make sure the adequate amount of stars is printed in one line
            print("*", end=" ")  # to make sure they are next to each other without a break
            # ending it with a space to have the same layout as the example provided
            # need to add something to make sure the columns are printed as well - only prints right amount of stars
        print()  # adding a newline to make sure they are printed in the "pairs" needed


# for every row in the range of (int given) it prints a newline
# for every row it prints row+1 stars - to give the triangle effect

print(triangle(rows))
