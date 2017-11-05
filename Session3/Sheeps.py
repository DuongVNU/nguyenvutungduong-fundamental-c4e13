size=[5, 7, 300, 90, 24, 50, 75]
print("Hello my name is Duong and these are my ship sizes\n", size)
a = size[0]
for i in range(7):
    if size[i] > a:
        a = size[i]
print("Now my biggest sheep has size",a,"let's shear it")
size[size.index(a)] = 8
print("After sheering, here is my flock:\n",size)
for i in range(7):
    size[i] = size[i] + 50
print("One month has passed, now here is my flock\n", size)
