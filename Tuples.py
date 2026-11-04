# Tuples

Fruits = ("Orange" , "Apple" ,"Banana" , "Guava")
print(type(Fruits))
print(Fruits)

Mix = ("Soham" , 21 ,True , "Male")
print(Mix)

print(Mix[2])

# Add items

Mix_List = list(Mix)

Mix_List.append("Tiwari ")

Mix = tuple(Mix_List)
print(Mix)

# deleting tuple

del Fruits
