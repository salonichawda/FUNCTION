age=int(input("enter the age:"))
def my_function():
    if age<14:
        print("kids drink toddy")
    elif age>14 and age<18:
        print("teens drink coke")
    elif age>=18 and age<21:
        print("young adult drink beer")
    else:
        print("adult drink whisky")
my_function()

