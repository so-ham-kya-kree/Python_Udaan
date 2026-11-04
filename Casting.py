# Casting 

# Converting into integer
x = "1234"

print(type(int(x))) # String is now converted into Integer

# Converting into float 
y = float(2) 

# Converting into String 
z = str(234)

# Converting List into Sets

li_1 = ["Supra" , "Porche" , " BMW" , "Mazda"]
print(type(li_1))

set_1 = set(li_1) # Casting into set

print(type(set_1))
print(set_1)

# Converting into Set to List

set_2 = list(set_1)
print(type(set_2))
print(list(set_2))

#Converting  pair into Dictionary

stu = [("Name" , "Soham") , ("Role" ,"Student") ]
print(type(stu))

print(dict(stu))
