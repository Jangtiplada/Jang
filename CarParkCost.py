#โปรแกรมคิดค่าที่จอดรถ
#เปิดบริการ 7:00 ถึง 23:00
#จอดรถไม่เกิน 15 นาที ไม่คิดค่าบริการ
#จอดเกิน 15 นาที แต่ไม่เกิน 3 ชม. คิดค่าบริการ ชม.ละ 10
#จอดรถตั้งแต่ 4 ชม.ถึง 6 ชม. คิดค่าบริการที่ 4-6 ชม.ละ 20 บาท
#จอดรถเกิน 6 ชม. ขึ้นไป เหมาจ่ายวันละ 200 บาท
InH=int(input())
InM=int(input())
OutH=int(input())
OutM=int(input())
timeH = (OutH - InH)
timeM = (OutM - InM)
MixH = (timeH * 10)

if  timeH >= 6 :
    print("200")

if  15 <= timeM  <= 59   :
    if timeM <= 15 :
        print("0")
    else:
        timeM > 15
        print(round(timeM / timeM * 10))



elif 3 >= timeH :

    if timeH >= 3 and timeM >= 1 :
        print(MixH+20)
    else:
        timeH >= 3
        print(MixH)
















