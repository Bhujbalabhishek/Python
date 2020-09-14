#Create dictionary which have key as a number and value as a its power of 2


dictionary = dict()

n = int(input("enter a number of values required"))

for i in range(1,n):
    dictionary[i] = i**2

print(dictionary)