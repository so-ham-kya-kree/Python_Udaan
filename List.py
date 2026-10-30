#list

li = ["Dog","Cat","Buffalo","Fox","Sheep","Camel"]
print("your elements are: " ,li)
print("first element: " ,li[0])
print("last ellement:" , li[-1])


#append 
#append is use to add element end of the list
li.append("Horse")
print(li)

#insert
#insert is used to add elements (between list 
li.insert(2,"Lion")
print(li)

#pop
li.pop(0)
print(li)


#remove
#remove is used to remove element from an element
li.remove("Lion")
print(li)


#slicing
print("Sliced elements : ",li[1:4])
print(li[:5])

#Extend 
new_li  = ["Ox" , "Zebra"]
li.extend(new_li) # extend is use to add multiple values at the end 
print(li)
