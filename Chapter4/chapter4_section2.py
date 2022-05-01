#manipulate strings with methods
#strings come bundled with special functions called string methods that can be used to work
#with and manipulate strings.

"Jean - luc Picard".lower()

#the dot(.) tells python that follows is the name of a method.

name = "Merve Zeynep"
name.lower()
name.upper()  # the opposite of the .lower() method is .upper()

loud_voice = "Can you hear me yet?"
loud_voice.upper()

#removing whitespace from a string
#there are three string methods that you can use to remove whitespace from a string:
# .rstrip() removes whitespace from the right side of a string.
# .lstrip()
# . strip()

name = "Jean-luc Picard       "
name.rstrip()

name = "      Jean-luc Picard"
name.lstrip()

name = "      Jean-luc Picard     "
name.strip()

#none of the three of them methods remove whitespace from the middle of the string.


#Determine if a string starts or ends with a particular string
#you can use two string methods to solve this problem : .startwith() and .endswith()

starship = "Enterprise"
starship.startswith("en")
starship.startswith("En")
starship.endswith("rise")


#string methods and immutability
name = "Picard"
name.lower()
name.upper()
#if you need to keep the result, you need to assign it to a variable:
name = name.upper()

