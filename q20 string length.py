def Name(name1,name2):
    if len(name1)>len(name2):
        print(name1)
    elif len(name1)<len(name2):
        print(name2)
    else:
        print(name1)
        print(name2)
name1=input("enter the name1:")
name2=input("enter the name2:")
Name(name1,name2)
