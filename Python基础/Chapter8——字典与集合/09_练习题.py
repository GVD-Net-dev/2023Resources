n1, n2 = [int(x) for x in input().split()]
d = dict()
for _ in range(n1):
    tmp1, tmp2 = input().split()
    if tmp1 in d.keys():
        d[tmp1].append(tmp2)
    elif tmp2 in d.keys():
        d[tmp2].append(tmp1)
    else:
        d[tmp1] = [tmp2]

for _ in range(n2):
    tmp = input().split()
    flag = 0
    for i in range(1, len(tmp)):
        if tmp[i] in d.keys():
            for j in d[tmp[i]]:
                if j in tmp:
                    flag = 1
                    break
        if flag == 1:
            break

    if flag == 1:
        print('No')
    else:
        print('Yes')
