#!/usr/bin/python3
#Write a program that counts the number of characters -
#in the word passed by the user and prints out the result

def counting(word):
    num = 0
    for i in word:
        num += 1
    print(num)

user_input = input("What is your word? ")
counting(user_input)

# simpler method
print(len(user_input))
