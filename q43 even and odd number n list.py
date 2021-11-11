list1=[1,2,2,5,8,4,4,8]
def my_function():
    i=0
    a=[]
    while i<len(list1):
        if list1[i]%2==0:
            a.append(list1[i])
        i+=1
    print(a,"even")
my_function()