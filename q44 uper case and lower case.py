string="The fuick Brow Fox"
def my_function():
    i=0
    count=0
    count1=0
    while i<len(string):
        if string[i]>="A" and string[i]<="Z":
            count+=1
            # print(count,"upercase")
        else:
            count1+=1
            # print(count,"lowercase")
        i+=1
    print(count,"uper case")
    print(count1,"lower case")
my_function()
