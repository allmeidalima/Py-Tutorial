#Modify Strings

p = "hello, word! "
b = "Banana12"

#upper() is a method used for transform all letters in capital letters 
print(p.upper())
#lower() is a method used for transform all letters in small letters
print(p.lower())
#this method is used for remove spaces in the beginning and the end
print(p.strip())
#this method change the letter for other
print(p.replace("H", "J"))
#Split() creates a list with the words in the chosen point 
print(p.split(","))
#capitalize() is a method that is used for transform the first letter in capital letters
print(p.capitalize())
#transform first letters in small letters
print(p.casefold())
#centralizes the string in the position determined
print(p.center(20, "$"))
#count the letters 
print(p.count(p))
#encode especial characters
print(p.encode())
#return TRUE if end is equal the parameter
print(p.endswith(" "))
#return TRUE if have one characters alphanumerics
print(b.isalnum())