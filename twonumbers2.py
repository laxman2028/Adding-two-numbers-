def add_without_plus_operator(a, b):
    while b != 0:
        data = a & b
        a = a ^ b
        b = data << 1
    return a
Num1 = int(input("Enter num1: "))
Num2 = int(input("Enter num2: "))
result = add_without_plus_operator(Num1,Num2)
print("Addition Of Two Numbers: ",result)
'''
b  != 0(T)
   data=0010 &1010= 0010
       a = 0010^1010 =0111
       b = 0010<<1=0100(decimal=4)
b!=0(T)
data = 0111&0100=0100
a      =0111^0100=1100
b      =0100<<1  =1000(8)

Repeat this process......'''

