#นางสาว ทิพลดา ภู่มาลา รหัส362515241005 กลุ่มเรียน EE36241N

print("--------Menu-------")
print("Welcome to Icecream Shop")
print("1.Strawberry = 80 THB")
print("2.Vanilla  = 50 THB")
print("3.Chocalate = 40THB")
print("4.Lemon    = 90 THB")
print("5.Milk   = 10 THB")
print("----------------------")
ch =int(input("Do you want : "))

if ch==1:
    price=80
    print("Your order:",ch,"price = ",price,"THB")
elif ch==2:
    price=50
    print("Your order:",ch,"price",price,"THB")
elif ch==3:
    price=40
    print("Your order:",ch,"price",price,"THB")
elif ch==4:
    price=90
    print("Your order:",ch,"price",price,"THB")
elif ch==5:
    price=10
    print("Your order:",ch,"price",price,"THB")
else:
    print("You not order")

