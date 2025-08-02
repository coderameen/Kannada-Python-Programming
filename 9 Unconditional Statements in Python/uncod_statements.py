for i in range(10):
    if i == 5:
        break
    print(i)

print("------------")
for i in range(10):
    if i==5:
        continue
    print(i)

print("----------------")
for i in range(10):
    if i==5:
        pass
    else:
        print(i)

print("-------------")
x = 10
if x > 5:
    pass  # Do nothing if x is greater than 5
else:
    print("x is 5 or less")
    