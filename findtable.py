x = 1
num = int(input("Enter a Number: "))
while x < 11:
    #Here we used str function to convert the value to string as we cant add str and int
    print(f"{x} X {num} = "+ str (x*num))
    x = (x+1)
