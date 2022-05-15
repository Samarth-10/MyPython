l=[1,2,3,4,5,6,7,8,9,10,15,16,12,25,35,44]
'''def divide(num):
    if num%5==0:
        return num'''
divide=lambda num:num%5==0
for i in l:
    l2=list(filter(divide,l))
print(l2)