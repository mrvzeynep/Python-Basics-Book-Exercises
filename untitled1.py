x = 100
y = 4
z = 40

answer = min(x ,y,z)
if x%2 != 0 :
    answer = x
if y%2 != 0 and y>answer : 
    answer = y
if z%2  != 0 and z>answer : 
    answer = z
print(answer)

#strings and input 
# the operator + is said to be overloaded because it has diffent meanin
#addition when applied to two numbers
#concatenation when applied to two strings 

#lenght function 
#len('abc')
