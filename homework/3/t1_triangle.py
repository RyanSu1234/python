"""
Topic:輸入三角形三邊，判斷是否能構成三角形，
　　　是三角形則顯示面積和周長，不行則顯示，無法構成三角形:

Circle Area formula:
p = 1/2 (a+b+c)
area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
e.g.
Show:a ="
Input1:3


Show:b ="
Input2:4
Show:c ="
Input3:5

output:
perimeter: 12.000000
Area: 6.000000
"""
import time
i=0
while i==0 or p<=0:
      a=input("請輸入三角形第一個邊長 ==> ")
      b=input("請輸入三角形第二個邊長 ==> ")
      c=input("請輸入三角形第三個邊長 ==> ")
      a=eval(a);b=eval(b);c=eval(c)
      s=0.5*(a+b+c)
      p=s*(s-a)*(s-b)*(s-c)
      if p<=0:
            print("此三角形不存在，請重新輸入!!!!")
      i+=1
else:
      print("三角形面積為：",p**0.5)


