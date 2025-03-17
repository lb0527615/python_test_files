def print_space(multiplier, string):
    print(multiplier*' '+string)
#the function here allows a set phrase or number under 'multiplier' to then multiply with the space and combine with anything set under 'string'.
def cascade_three(cascade):
    print_space(0, cascade)
    print_space(1, cascade)
    print_space(2, cascade)
#this function uses the formula from the print_space function and is written out three times. multiplier is defined by the numbers 0, 1, and 2 to allow multiplication of the space. cascade is not defined yet, but can be if cascade_three is executed.
cascade_three('season')
#This is the second function being executed, where cascade is defined as season.