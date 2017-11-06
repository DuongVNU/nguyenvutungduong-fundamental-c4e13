hinhve = [
"""
_________
  |     |
  |     O
  |
  |
 _|_
"""
,
"""
_________
  |     |
  |     O
  |     |
  |
 _|_
"""
,
"""
_________
  |     |
  |     O
  |   --|
  |
 _|_
"""
,
"""
_________
  |     |
  |     O
  |   --|--
  |
 _|_
"""
,
"""
_________
  |     |
  |     O  Help meeee!!
  |   --|--
  |    /
 _|_
"""
,
"""
_________
  |     |
  |     O  Axx!!
  |   --|--
  |    / \\
 _|_


"""
]

dem1 = 0
dem3 = 0
tu = input("Nhập từ bạn muốn đoán:")
b = list(tu)
d = []

for i in range(len(b)):
    d.append("_")
print(*d, sep = " ")
#Guess
for j in range(1000):
    dem2 = 0
    key = input("Nhap chu cai ban doan: ")
    for i in range(len(b)):
        if key == b[i]:
            d[i] = key
            print(*d, sep = "  ")
            dem1 += 1
        elif key != b[i]:
                dem2 = dem2 + 1
    if dem2 == len(b):
        print(hinhve[dem3])
        dem3 = dem3 + 1
    if dem1 == len(b):
        print("Chúc mừng bạn đã chiến thắng ^o^")
        exit()
    if dem3 == 6:
        print("Bạn đã thua =_=")
        exit()
