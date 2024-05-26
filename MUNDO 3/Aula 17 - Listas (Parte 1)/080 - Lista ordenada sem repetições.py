list = []
num = 0
for x in range(0, 5):
    num = int(input())
    if x == 0 or list[x-1] < num:
        list.append(num)
    else:
        for y in range(0, x):
            if list[y] > num:
                list.insert(y, num)
                break
print(list)
