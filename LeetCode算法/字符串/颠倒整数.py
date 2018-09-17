x=1230
if(x<0):
    flag=-1;
else:
    flag=1;
s=str(abs(x))
x1=flag*int(s[::-1])#反转字符串
if(x1>-2**31 and x1<2**31-1):
    print(x1)
else：
    print(0)
