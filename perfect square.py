e = int(input("PUT IN YOUR NUMBER: "))
answer = [0]
for i in range(1, e+1):
    x = i ** 2
    if x == e:
        answer.append(x)
if len(answer) == 2:
    print(True)
else:
    print(False)