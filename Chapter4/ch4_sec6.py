
#streamline your print statements
name = "Zaphod"
heads = 2
arms = 3
print(name , "has" ,  heads , "heads" , "and" , arms , "arms.")
print(name + " has "  + str(heads)  + " heads and "  + str(arms) + " arms.")

#both techniques produce code that can be hard to read. trying to keep track of what goes inside or
#outside of quotes can be tough. fortunately, there's a third way of combining string : formatted string literals
#f-strings

print(f"{name} has {heads} heads and {arms} arms.")
#the string literal starts with the letter f before the opening quotation mark.
#variable names surrounded by curly braces ara replaced with their corresponding values using str()

n = 3
m = 4
print(f"{n} times {m} is {n*m}")

#exercise 1 
weight = 0.2
animal =  "newt"
print(str(weight) + " is the weight of the " + animal + ".")
print("{} is the weight of the {}".format(weight, animal))
print(f"{weight} is the weight of the {animal}.")


#find a string in a string
#one of the most useful string method is .find()
#commonly referred to as a substring.

phrase = "the surprise is in here somewhere"
phrase.find("surprise")

# the value that .find() returns is the index of the occurence of the string you pass to it. 
#in this case, "surprise" starts at the fifth character which has index 4 because counting starts at 0.
#if .find() does not find the desired substring, it will return -1 instead.

"the surprise is in here somewhere".find("surprise")
"the surprise is in here somewhere".find("SURPRISE")
#the find method only accepts a string as its input. 

my_story = "I'm telling you the truth; nothing but the truth!"
my_story = my_story.replace("the truth" ,  "lies")


text = "some of the stuff"
new_text = text.replace("some of" , "all")
new_text = new_text.replace("stuff", "things")

#exercise 1 
new_string= "AAA"
new_string.find("a")

#exercise 2 
new_variable = "Somebody said something to Samantha."
new_variable.replace("s", "x")

#exercise 3 

new_input = input("please enter your new input: ")
print(new_input.find("e"))














