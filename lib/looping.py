#!/usr/bin/env python3
#Write a function fizzbuzz() that prints the numbers from 1 to 100. 
# For multiples of three, print "Fizz" instead of the number and for the multiples of five print "Buzz". 
# For numbers which are multiples of both three and five, print "FizzBuzz".

def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")
    
def square_integers(int_list):
    return [x**2 for x in int_list]

def fizzbuzz():
    for x in range(1, 101):
        output = ""
        
        if x % 3 == 0:
            output += "Fizz"
        
        if x % 5 == 0:
            output += "Buzz"
        
        if output == "":
            output = str(x)
        
        print(output)
