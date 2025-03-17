def is_square(x, y):
    if x**2 == y:
        return True
    #This line of code is the first function that will run to see if one variable given is the square root of the other variable given.
    elif y**2 == x:
        return True
    #This line of code creates an alternative that carries out the same function as the first line of code, only that it will look for the square root if the user input the two variables in different locations of the code.
    else:
        return False
    #If neither of the two lines of code above can find if one of the variables is the square root of the other variable, automatically it will consider neither being the square root of the other variable, and will consider it False.
#The above prompt allows the user to find if one variable is the square root of the other variable. It requires the user to use (print(is_square()) to calculate.