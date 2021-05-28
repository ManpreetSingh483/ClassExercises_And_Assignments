import ProgramFirst_Module
import ProgramThird_Module

# Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.

def reverse_name():

    name = input("Enter First and Last Name ")
    reversedName =''
    index = len(name)
    while(index>0):
        reversedName = reversedName + name[index-1]
        index =index -1
    print('Name in Reverse Order is :',reversedName)

ProgramFirst_Module.calculate_circleArea()
ProgramThird_Module.display_currentDateTime()
