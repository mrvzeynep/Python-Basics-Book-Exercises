
#exercise 1
new_variable = "34"
new_variable1 = int(new_variable)
print(type(new_variable1))
print(new_variable1 * 3)


#exercise 2
variable = "7.05"
variable1 = float(variable)
print(type(variable1))
print(variable1 * 2)

#exercise 3
object_int = 456453
object_str = " deneme"
print(str(object_int) + object_str)

#exercise 4
number1 = int(input("Enter your first number please : "))
number2 = int(input("Enter your second number please : "))
print("The product of" , number1, "and" , number2 , "is" , float(number1*number2),".")
print("The product of " + str(number1) +" and " + str(number2) + " is " + str(float(number1*number2)) + ".")