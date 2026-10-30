# #Calculator

print("Calculator")
nm1 = int(input("Enter number One : "))
nm2 = int(input("Enter Second Number: "))
operator = input("Enter operator : ")

# if-Ladder

if operator == "+" :
    print(nm1 + nm2)
elif operator == "-" :
    print(nm1 - nm2)
elif operator == "*" :
    print(nm1 * nm2)
elif operator == "/" :
    print(nm1 / nm2)
elif operator == "%" :
    print(nm1 % nm2)
elif operator == "**" :
    print(nm1 ** nm2)
else:
    print("Enter valid operator")