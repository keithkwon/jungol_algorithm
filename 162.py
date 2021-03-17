numbers = list(map(int, input().split()))

for i in range(9):
    numbers[i+2] = (numbers[i] + numbers[i+1]) %10


print(numbers)