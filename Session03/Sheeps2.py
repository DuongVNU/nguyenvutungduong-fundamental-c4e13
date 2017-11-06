size=[5, 7, 300, 90, 24, 50, 75]
n = int(input("Enter month:"))
print("Hello my name is Duong and these are my ship sizes\n", size)
for i in range(n):
    print("MONTH", i + 1,":")
    for j in range(7):
        size[j] = size[j] + 50
    print("One month has passed, now here is my flock\n", size)
    a = size[0]
    for j in range(7):
        if size[j] > a:
            a = size[j]
    print("Now my biggest sheep has size",a,"let's shear it")
    size[size.index(a)] = 8
    print("After sheering, here is my flock:\n",size)
    print("\n")
total = 0
for i in range(7):
    total = total + size[i]
print("My flock has size in total:", total)
print("I would get {0} * 2$ = {1}$".format(total, total * 2))
