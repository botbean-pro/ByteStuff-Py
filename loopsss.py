import time as t
rows = 7
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end="")
        t.sleep(0.5)
    print()

for i in range(1, rows + 1):
    for j in range(rows - i + 1):
        print("*", end="")
        t.sleep(0.5)
    print()