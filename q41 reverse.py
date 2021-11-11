string="123abcd"
def my_function():
    i=len(string)-1
    while i>=0:
        print(string[i],end=" ")
        i-=1
my_function()