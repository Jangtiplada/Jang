
#จงเขียนโปรแกรมคำนวณหาความยาวของด้านที่สามของสามเหลี่ยม เมื่อเราทราบความยาวด้านสองด้าน(a กับ b)และมุมระหว่างด้านสองด้านนั้น(C)ซึ่งคำนวณได้จาก Law of Cosines
#สูตร c= math.sqrt((a**2)+(b**2)-(2*a*b*math.cos(C)))


import math
a = float(input())
b = float(input())
D= float(input())
C = D*math.pi/180
c= math.sqrt((a**2)+(b**2)-(2*a*b*math.cos(C)))
print("c=",c,"(cm.)")