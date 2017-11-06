from turtle import *
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
shape("turtle")
b = 3
for i in range(5):
    color(colors[i])
    for i in range(b):
        forward(100)
        left(360/b)
    b = b + 1
mainloop()
