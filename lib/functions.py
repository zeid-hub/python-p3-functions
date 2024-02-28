#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")
greet_programmer()

def greet(name):
    print(f"Hello, {name}!")
greet("Zeid")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")
greet_with_default("Harith")

def add(num1, num2):
    sum = num1 + num2
    print(sum)
    return sum
add(40, 500)    

def halve(number):
    my_half = number/2
    print(my_half)
    return my_half
halve(8)    