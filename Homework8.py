"""
Analysis
1.input คือ การนำข้อมูลเข้าทางแป้นพิมพ์ โดยป้อนตัวเลข10 ตัว
2.process คือ เป็นการนำข้อมูลทั้ง 10 ตัว มาบวกกันทั้งหมด
3.output คือ การแสดงผลรวมของทั้ง10ตัว
4.Define a  Variable คือการกำหนดตัวแปร ในแต่ละข้อมูลเพื่อรับค่าและแสดงผลของค่านั้น
"""
n = 10
total = 0.0
for i in range(n):
    number = float(input("Enter number :"))
    total = total + number
print(total)
