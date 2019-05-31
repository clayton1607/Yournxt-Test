num=input("Enter the integer \n")
def palindrome(num):
    if str(num) == str(num)[::-1]:
        #reverse the num 
        return True
    else:
        return False
i=1
try:
    while True:
        val=int(num)
        if (palindrome(val-i)):
            print("Output:"+str(val-i))
            break
        if (palindrome(val+i)):
            print("Output:"+str(val+i))
            break
        i+=1
except ValueError:
    print("Enter Valid Integer")


# Output:
# python3 closestPalindrome.py 
# Enter the integer 
# 123
# Output:121
# (WebDev) clayton@clayton-hp:~/TE-2018-2019/Python$ python3 closestPalindrome.py 
# Enter the integer 
# df1
# Enter Valid Integer