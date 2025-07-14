numbers = [6,5,3,8,4,2,5,4,11]

sum = 0

for val in numbers :
    if val % 2 == 0 :
        print("Even",val)
    else :
        print("Odd",val)
    sum = sum+val
print("THE sum is ", sum)

