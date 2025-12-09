hi=input("enter the string")
vowels={"a":0,"e":0,"i":0,"o":0,"u":0}
for C in hi:
    if C in vowels:
        vowels[C]=vowels[C]+1

print(vowels)