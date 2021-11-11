num=int(input("enter the number:"))
def my_function():
    b=0
    i=1
    while i<=num: 
        if num%2==0:
            b+=1
        i+=1
    if b==2:
        print(num,"prime")
    else:
        print(num,"not prime")
my_function()




num=int(input("enter the number"))
def my_function():
    i=0
    while i<=num:
        b=0
        j=1
        while j<=num:
            if i%j==0:
                b+=1
            j+=1
        if b==2:
            print(i,"prime")
        else:
            print(i,"not prime")
        i+=1
my_function()