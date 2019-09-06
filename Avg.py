sum = 0
count = 0
n = float(input("enter number"))
while n != -1:
    sum += n
    count = count + 1
    n = float(input("enter number"))
avg = sum / count
print(avg)