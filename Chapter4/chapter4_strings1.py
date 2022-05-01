#string and string methods
#collection of text in python are called strings. 
#special functions called string methods are used to manipulate strings.

#the string data type 
#strings are fundamental pyhton data types.
#strings are used to represent text.

#print(type("hello, world"))

phrase= "hello, world"
print(type(phrase))

string1 ='hello, world'
string2 = "1234"
#whenever you are create a string by surrounding text with quotation marks, 
#the string is called a string literal.
#the quotes surrounding a string are called delimiters because they tell pyhton
#where a string begins and where it ends.

#determine the length of a string
len("abc")

letters =  "abc"
num_letters = len(letters)
num_letters

#multiline strings
#pep 8's 79-character line-legth is recommended

paragraph = "this planet \
this : most the people \
living on it"

long_string = "this multiline string is \
displayed on one line"

#multiline strings can also be created using triple quotes as delimeters ("""or''')

#concatenation, indexing, and slicing
string1 = "abra"
string2 = "cadabra"
magic_string =  string1 + string2
magic_string



first_name = "arthur"
last_name = "dent"
full_name = first_name + " " + last_name

#string indexing
flavor = "apple pie"
print(flavor[1])
print(flavor[0])
print(flavor[-1])


#string slicing
first_three_letters = flavor[0] + flavor[1] + flavor[2]

flavor[0:3]

#strings are immutable
word = "goal"
#word[0] = "f"
 #if you want to alter a string, you must create an entirely new string.
 #to chage the string "goal" to the string "foal"
 
word = "goal"
word = "f" + word[1:]
 


















