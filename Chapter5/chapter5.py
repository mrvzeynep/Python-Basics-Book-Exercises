#numbers and math
#python has three built-in number data types : integers, floating-point  numbers, and complex numbers

type(1) #int
int("25")

#an integer literal is an integer value that is written explicitly in your code
#integer literals can be written in two different ways:
    
10000 # straightforward 
1_000_0 #when you write large numbers by hand, you can use an underscore

#there is no limit to how large an  integer can be, which might be surprising considering computers
#have finite memory.


#floatig-point numbers
type(1.0)
float("1.24")

1000000.0
1_000_000.0
1e6   # for really large numbers, you can use E-notation. (exponential notation)
2e+17 # the + sign indicates that the exponent 17 is a positive number.
200000000000000000.0
0.0001
1e-4 # is interpreted as 10 raised to the power -4, whic is equal to 0.0001

#unlike integers, floats do have a maximum size. the max floating-point number depends on your system
#but something like 2e400 ought to be well beyond most machines's capabilities.
2e400
-2e400

#exercise 1
num1 = 25_000_000
num2 = 25000000
print(num1)
print(num2)

#exercise 2
#num  = 175_000.0
num = 175e3
print(num)

#exercise 3


#aritmetic operators and expressions
1 + 2 
1.0 + 2
1- -3
1 --3
int(5.0 / 2)
9 // 3 

#exponents
2 ** 2
3 ** 1.5
9 ** 0.5
2 ** -1

#the modulus operator 
5 % 3














