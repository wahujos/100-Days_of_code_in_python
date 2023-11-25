#!/usr/bin/python3
#solution one
##Don't change the code below

two_digit_number = input("Type a two digit number:  ")
##Don't change the code above

first = int(two_digit_number)/10
second = int(two_digit_number) % 10
value = first + second
print(int(value)) 

#solution2
##Don't change the code below

two_digit_number = input("Type a two digit number:  ")
##Don't change the code above

#Always remember that the input received from the user is of type str.
print(type(two_digit_number))
first_num = int(two_digit_number[0])
second_num = int(two_digit_number[1])
sum_value = first_num + second_num
print(sum_value)
