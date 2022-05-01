m1 = 0.1
m2 = 0.2
print(m1 + m2) # is ihis a bug in python? no it isn't a bug. it's floating - point representation error,
#and it has nothing to do with python.

# math functions and number methods
#python has a few built-in functions you can use to work with numbers.
#round() for rounding numbers to some number of decimal places
#abs () for getting the absolute value of a number
# pow() for raising a number to some power

round(2.3)
round(2.7)
round(2.5)
round(3.5) 
# python 3 rounds numbers according to a strategy called rounding ties to even.
# if that digit is even, you round down. if the digit is odd, you round up.

round(3.14159 , 3) #rounded 3 decimal places
round(2.71828 , 2) # rounded 2 decimal places

abs(3)
abs(-5)
abs(-5.0)

pow(2 , 3)

pow(2 , -2)

#the pow() function accepts an optional third argument.
#pow(x,y,z) is equivalent to (x ** y) % z

pow(2, 3, 2)

#check if a float is integer

num = 2.5
num.is_integer()

#is_integer method can be useful for validating user input. 

#exercise 1
number = float(input("Enter a number : "))
print(f"{number} rounded to 2 decimal places is {round(number, 2)}")

#exercise 2 
prompt_1 = int(input("Enter a number  : "))
print(f"The absolute value of {prompt_1} is {float(abs(prompt_1))}")

#exercise 3


sample_1 = float(input("Enter a number : "))
sample_2 = float(input("Enter another number : "))
the_difference = (sample_1 - sample_2)
print(f"The difference between {sample_1} and {sample_2} is an integer ? {the_difference.is_integer()}")


#print numbers in style 
n = 7.125
f"The value of n is {n}"
f"The value of n is {n: .2f}"

#the colon (:) after the variable n indicates that everything after it is 
#part of  the formatting specification. the .2 in .2f rounds the number to two decimal places,
#and the f tells pyhton to display n as a fixed-point number.

n = 1 
f"The value of n is {n : .2f}"
f"The value of n is {n : .3f}"

n = 1234.56
f"the value of n is {n : ,.2f}"

balance = 2000.0
spent = 256.35
remaining = balance - spent
f"After spending ${spent : .2f} , I was left with ${remaining : ,.2f}"


ratio = 0.9
f"Over {ratio : .1%} of Pythonistas say 'Real Python rocks!"

f"Over {ratio : .2%} of Pythonistas say 'Real Python rocks!"







