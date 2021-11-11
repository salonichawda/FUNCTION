# list=["saloni","mom","nayan"]
# i=0
# length=len(list[i])-1
# a=[]
# sum=0
# sum1=0
# while i<len(list):
#     j=length
#     while j>0:
#         a.append(list[i])
#         j-=1
#     if list[i]==a[i]:
#         sum+=1
#     else:
#         sum1+=1        
#     i+=1
# print(sum)
# print(sum1)


def list_change(list1,list2):
    i=0
    a=[]
    while i<len(list1):
        a.append(list1[i]*list2[i])
        i+=1
    print(a)
list_change([5, 10, 50, 20], [2, 20, 3, 5])



list1=["saloni",23,3.4,"ranu",45,"ashu",57.0]
i=0
while i<len(list1):
    if type(list1[i])==str:
        print(i,list1[i])
    i+=1