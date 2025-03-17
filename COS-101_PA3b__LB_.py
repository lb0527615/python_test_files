def print_sums(n, current_sum=0, current_number=1):
    if current_number <= n:
        current_sum += current_number
        print(current_sum)
        print_sums(n, current_sum, current_number + 1)
        #The above function allows the user to input a function, which will do a chain of numbers that will stop at the specified number.
n = int(input("Enter a natural number:"))
#The above function will ask the user to input a natrual number.
print(print_sums(n))
#When given an answer, the console will respond by performing the print_sums function.