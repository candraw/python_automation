import random

i = input("Enter password length (max 71) : ")
length = int(i)

#content
number = '1234567890'
lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbol = '!@#$%^&*'

def generate():
    combined = f"P{number}{lowercase}{uppercase}{symbol}"
    random_string = "".join(random.sample(combined, length))
    print("Your Password is : ", (random_string))

generate()

while True:
    i2 = input("Are You Ok with the password ? : y/n ")
    answer = i2
    if (answer == 'y'):
        print("Done!")
        break
    elif(answer == 'n'):
        generate()
