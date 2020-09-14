#Program to accept the strings which contains all vowels

def check_vowel(string):
    str = string.lower()

    vowels = set("aeiou")

    val = set()

    for char in str:
        if char in vowels:
            val.add(char)
        else:
            pass

    if len(val) == len(vowels):
        print("string is accepted")
    else:
        print("string is not accepted")

string =input("enter a string")
check_vowel(string)