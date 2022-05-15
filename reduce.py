from functools import reduce


l=[43,58,3,59,85,34,556,12,34,55,30005,34]
def greater(num1,num2):
    if num1>num2:
        return num1
    else:
        return num2
l2=reduce(max,l)
print(l2)