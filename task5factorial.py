num=int(input("Enter number: "))
def factorial(num):
    if num<2:
        return 1
    else:
        return num*(factorial(num-1))
result=factorial(num)
print("factorial of",num,"is: ",result)