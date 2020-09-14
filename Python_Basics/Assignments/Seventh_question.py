#Check if input number is Palindrome numbers or not



def check_Palindrome_num(num):
    temp = num
    rev = 0
    while num>0:
        dig =num%10
        rev =rev*10+dig
        num =num//10

    if temp==rev:
        print("palindrome")
    else:
        print("not palidrome")

num = int(input("enter a number "))
check_Palindrome_num(num)