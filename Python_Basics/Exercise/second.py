"""In many jurisdictions a small deposit is added to drink containers to
encourage people to recycle them. In one particular jurisdiction, drink containers
holding one liter or less have a $0.10 deposit, and drink containers holding 
more than one liter have a $0.25 deposit. Write a program that reads the number 
of containers of each size from the user. Your program should continue by computing 
and displaying the refund that will be received for returning those containers. 
Format the output so that it includes a dollar sign and always displays exactly
two decimal places"""

#taking input from user in the int format 
small_Container = int(input("Enter the no.of small containers you want to recycle?"))

large_Container = int(input("Enter the no.of large containers you want to recycle?"))

#computing the refund using both small and large container
refund = (small_Container * 0.10) + (large_Container * 0.25)

#displaying the refund in the format having two decimal places with '$' sign 
print("Total refund for returning the both Containers is $" + "{0:.2f}".format(float(refund)))