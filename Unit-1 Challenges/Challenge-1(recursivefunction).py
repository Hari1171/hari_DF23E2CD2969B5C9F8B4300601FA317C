def factorial(x):
    if x==1:
        return 1
    else:
        return x*factorial(x-1)
num = int (input("Enter the number:"))
res=factorial(num)
print("The Factorial of{} is {}.".format(num,res))