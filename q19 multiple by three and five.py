def shownumber(limit):
    i=1
    sum=0
    while i<=limit:
        if i%3==0 or i%5==0:
            sum+=i
            # print(i)
        i+=1
    print(sum,"sum")
shownumber(int(input("enter the limit:")))




