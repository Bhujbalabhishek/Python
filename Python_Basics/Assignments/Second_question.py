
# 1st pattern
for i in range(5):
    for j in range(5):
        print("*", end=" ")
    print()

print()

#2nd pattern
for i in range(5):
    for j in range(5):
        print(1, end=" ")
    print()

print()

# 3rd pattern
for i in range(5):
    for j in range(5):
        if i%2 == 0:
            print(0, end=" ")
        else:
            print(1, end=" ")
    print()

print()


# 4th pattern pending (done)
for i in range(5):
    i=i+1
    for j in range(i):
        if (i+j)%2 == 0:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()

print()

# 5th pattern
for i in range(5):
    i = i+1
    for j in range(i):
        if j % 2 == 0:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()

print()

# 6th pattern
for i in range(5):
    for j in range(5):
        j=j+1
        print(j, end=" ")
    print()

print()


# 7th pattern pending
num =1
for i in range(1,6):
    for j in range(1,6):
        num = str(num).zfill(2)
        print(num,end=" ")
        num=int(num)+1
    print()

print()

# 8th pattern
for i in range(5,0,-1):
    for j in range(i):
        if j % 2 == 0:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()

print()
#9th pattern

for i in range(0,5):
    for k in range(0,5-i-1):
        print(end=" ")
    for j in range(0,i+1):
        print(1,end=" ")
    print()

print()


# 10th pattern

for i in range(5):
    for j in range(7):
        if (j==0 or j==6) or (i==0 and j==1 or i==0 and j==5) or (i==1 and j==2 or i==1 and j==4) or (i==2 and j==3):
            print("*", end="")
        else:
            print(end=" ")
    print()

print()

# 11th pattern

for i in range(1,4):
    for j in range(1,6):
        j =j*i
        j = str(j).zfill(2)
        print(j,end=" ")
    print()
    for k in range(5,0,-1):
        k=k*i
        k = str(k).zfill(2)
        print(k,end=" ")
    print()

print()
# 12th pattern


for i in range(1, 8):
    for j in range(1, i):
        print(2 ** j, end=" ")
    print("")

print()

# 13th pattern
n = int(input("enter a number"))
for i in range(n):
    s = "-".join(chr(ord('a')+n-j-1)
    for j in range(i+1))
    print((s+s[::-1][1:]).center(n*4-3, '-'))

for i in range(n-1):
    s = "-".join(chr(ord('a')+n-j-1)
    for j in range(n-i-1))
    print((s+s[::-1][1:]).center(n*4-3, '-'))

# for i in range(n):
#     print(" "*(n-i-1)+"a" *(i+1))
# for j in range(n-1,0,-1):
#     print(" "* (n-j)+"a" * j)