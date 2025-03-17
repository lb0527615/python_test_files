def number(x, y):
    z = x
    result = 0
    #0 is assigned to result so it can remain an integer function that will constantly be changed to assist in the while loop.
    while z <= y:
        result += z
        z += 1
    return result
    #The above while loop will find the sum of all the integer functions given under x and y.
x = int(input('Enter first positive integer:'))
y = int(input('Enter second positive integer:'))
#The above two lines will ask the user to input two seperate integer functions, which will be assigned to x and y.
print(number(x, y))