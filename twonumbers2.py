def add_without_plus_operator(a, b):
    while b != 0:
        data = a & b
        a = a ^ b
        b = data << 1
    return a
print(add_without_plus_operator(2, 10))
print(add_without_plus_operator(-20, 10))
print(add_without_plus_operator(-10, -20))
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

