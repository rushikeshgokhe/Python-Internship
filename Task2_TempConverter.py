temp = input("Enter temperature (e.g., 25C or 77F): ")

unit = temp[-1]
value = float(temp[:-1])

if unit == 'C' or unit == 'c':
    f =  (value* 9/5) + 32
    print(value,"in C to ",f,"in F",sep=" ")
elif unit == 'F' or unit == 'f':
    c = (value- 32) * 5/9
    print(value,"in F to ",c,"in C",sep=" ")
else:
    print("Invalid unit. Use 'C' or 'F'.")
