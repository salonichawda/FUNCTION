def my_function(speed):
    if speed<=70:
        print("ok")
    elif speed>70:
        a=speed-70
        points=a/5
        print(points)
    elif points>12:
        print("licence suspended")
my_function(int(input("enter the speed:")))