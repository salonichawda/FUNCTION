def my_function(list1):
    i=0
    min=list1[i]
    while i<len(list1):
        if list1[i]<min:
            min=list1[i]
        i+=1
    print(min)
my_function([34,6,1,78,4,7,90])