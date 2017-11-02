n = int (input("Nhap n:"))
m = int (input("Nhap m:"))
print("a)")
for i in range(n):
    print("*", end=" ")
print("\n")


print("b)")
for i in range(1, n + 1):
    if i % 2 == 0:
        print("*", end="")
    else:
        print("x", end="")
print("\n")


print("c)")
print("Hello Techkids")
print("")
print("I love you")


print("d)")
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if (i + j) % 2 == 0:
            print("x",end="")
        else:
            print("*",end="")
    print("\n")
