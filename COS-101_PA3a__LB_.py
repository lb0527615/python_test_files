x = int(input('Enter an integer in 1-20 range:'))
#the above function asks the user to input a variable between 1 and 20
if 1<x<10:
    print('It is between 1 and 10 (inclusive).')
#The above function will tell the user their answer was in between 1 and 10.
elif 11<x<20:
    print('It is between 11 and 20 (inclusive).')
#The above function will tell the user their answer was in between 11 and 20.
else:
    print('It is not in the specified range.')
#The above function will tell the user their answer wasn't in the specified range.