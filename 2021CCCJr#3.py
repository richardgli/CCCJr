l = []
while True:
    number = input()
    if number == "99999":
        break
    l.append(number)

for i in range(len(l)):
    sum = int(l[i][2] + l[i][3] + l[i][4])
    if (int(l[i][0]) + int(l[i][1])) % 2 != 0:
        print("left", sum)
        prev = "left"
    elif (int(l[i][0]) + int(l[i][1])) % 2 == 0 and (int(l[i][0]) + int(l[i][1])) != 0:
        print("right", sum)
        prev = "right"
    elif (int(l[i][0]) + int(l[i][1])) == 0:
        print(prev, sum)

