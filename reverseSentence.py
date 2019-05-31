inputString= input("Input:")
outputString= ""
n=len(inputString)
i=n-1

while i>-1:
    tempString=""
    if inputString[i]==" ":
        i-=1
        continue
    while inputString[i]!=" " and i>-1:
        tempString+=inputString[i]
        i-=1
    if outputString=="":
        outputString+=tempString[::-1]
        # for first word no space
    else:
        outputString+=" "+tempString[::-1]
    #print(outputString+" "+str(i))
    i-=1
print("Output:"+outputString)


# Output:
# python3 reverseSentence.py 
# Input:     HELLO WORLD TODAY IS a good day
# Output:day good a IS TODAY WORLD HELLO