a = input("Введите число")
b = a[len(a) - 3:]
a = a[: len(a) - 3]
while a != "":
    if len(a) >= 3:
        end = a[len(a) - 3:]
        a = a[: len(a) - 3]
    else:
        end = a
        a = ""
    b = end + " " + b

print(b) 
