def my_function(list1):
    i=0
    max=list1[i]
    while i<len(list1):
        if list1[i]>max:
            max=list1[i]
        i+=1
    print(max)
my_function([1,34,6,78,4,7,90])