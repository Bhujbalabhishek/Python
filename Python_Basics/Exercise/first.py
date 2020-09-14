# Create a program that displays your name and complete mailing address formatted 
# in  the manner that you would usually see it on the outside of an envelope. 
# Your program does not need to read any input from the user

# print("Abhishek Bhujbal")
# Abhishek Bhujbal
# Swagat CHS A/3, 1/6, 
# Sector-24, Nerul,
# Navi Mumbai-400706



# creating a dictionary having key and value pairs  
info = {'name':"Abhishek Bhujbal,", 'building_No':"Swagat CHS, A/3, 1/6,", 'locality':"Sector-24,Nerul,", 'area':"Navi Mumbai-400706"}

#iterating ingo dictionary into for loop for getting desired output
for key, value in info.items():
    print(value)