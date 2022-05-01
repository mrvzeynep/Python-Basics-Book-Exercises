#exercise 1
list = ["Animals" , "Badger" , "Honey Bee" , "Honeybadger"]
print(list[0].lower())
print(list[1].lower())
print(list[2].lower())
print(list[3].lower())

#exercise 2 
list = ["Animals" , "Badger" , "Honey Bee" , "Honeybadger"]
print(list[0].upper())
print(list[1].upper())
print(list[2].upper())
print(list[3].upper())

#exercise 3

string1 = "    Filet Mignon"
string1.lstrip()

string2 = "Bristet    "
string2.rstrip()

string3 = "    Cheeseburger    "
string2.strip()


#exercise 4

string1 = "Becomes"
string2 = "becomes"
string3 = "BEAR"
string4 = "   bEautiful"

print(string1.startswith("be"))
print(string2.startswith("be"))
print(string3.startswith("be"))
print(string4.startswith("be"))


#exercise  5
string1 = "Becomes"
string2 = "becomes"
string3 = "BEAR"
string4 = "   bEautiful"


print(string1.lower().startswith("be"))
print(string2.startswith("be"))
print(string3.lower().startswith("be"))
print(string4.lstrip().lower().startswith("be"))
