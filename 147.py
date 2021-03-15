n = int(input())

count = 0

for i in range(n):
    for j in range(i):
        print(' ', end='')
    for j in range(n- i):
        print(count, end = ' ')
