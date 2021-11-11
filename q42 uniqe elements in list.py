list=[1,2,2,5,8,4,4,8]
def unique():
    i=0
    a=[]
    for i in list:
        if i not in a:
            a.append(i)
        i+=1
    print("unique values=",a)
unique()
