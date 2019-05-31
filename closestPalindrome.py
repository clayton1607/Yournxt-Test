num=input("Enter the integer \n")
def palindrome(num):
    if str(num) == str(num)[::-1]:
        return True
    else:
        return False
i=0
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
