#!/usr/bin/python3
#Calculating the body mass index
##  Dont change the code below
height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

##Dont change the code above
height = float(height)
weight = float(weight)
Bmi = weight / (height * height)
print(int(Bmi))
