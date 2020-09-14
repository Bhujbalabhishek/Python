
# without using built in function find max and min between 10 numbers
num = [50,60,80,25,45,62,90,88,99,100]
print(num)
print(type(num))

largest = num[0]
for i in num:
    if i > largest:
        largest = i
print(largest)

smallest = num[0]
for j in num:
    if j < smallest:
        smallest = j
print(smallest)

# with using built in function find max and min between 10 numbers
print(max(num))
print(min(num))