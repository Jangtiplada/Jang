'''
Analysis
1.input คือ การนำข้อมูลเข้าทางแป้นพิมพ์ โดยป้อนตัวเลขเข้าเรื่อยๆ จนกว่าจะเจอ -1 ถึงหยุดรับข้อมูล
2.process คือ เป็นการนำข้อมูลทั้งหมด มาหาค่าเฉลี่ยโดยไม่รวม -1
3.output คือ การแสดงผลของค่าเฉลี่ย
4.Define a  Variable คือการกำหนดตัวแปร ในแต่ละข้อมูลเพื่อรับค่าและแสดงผลของค่านั้น
'''
sum = 0.0
n = 0
number = int(input("Enter number :"))
while number > -1:
    sum = sum + number
    n = n + 1
    number = int(input("Enter number :"))
avg = sum / n
print("Avg =", avg)