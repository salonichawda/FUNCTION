# def check_numbers(num1,num2):
#     if num1%2==0 and num2%2==0:
#         print("dono numbers even hai")
#     else:
#         print("dono numbers even nhi hai")
# num1=20
# num2=11
# check_numbers(num1,num2)



def check_numbers(num1,num2):
    i=0
    while i<len(num1):
        if num1[i]%2==0 and num2[i]%2==0:
            print("dono number even hai")
        else:
            print("dono number even nhi hai")
        i+=1
check_numbers([2, 6, 18, 10, 3, 75],[6, 19, 24, 12, 3, 87])

