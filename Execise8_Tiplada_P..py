#นางสาว ทิพลดา ภุ่มาลา รหัส362515241005 กลุ่มเรียน EE36241N

usernameinput =input ("username :")
passwordinput =input ("password :")
if usernameinput == "Tiplada" and passwordinput == "01072543":
    print("^^^^welcome to JANG Beauty Cosmetics^^^^")
    print("---Which product would you like to receive?---")
    print("       List of all products     ")
    print("-----------------------------------")
    print("1.แป้ง CHANEL        = 350 THB")
    print("2.ลิปสติก MAC         = 490 THB")
    print("3.อายแชดดว์ NYX      = 725 THB")
    print("4.คุชชั่น SIVANNA      = 360 THB")
    print("5.ดินสอเขียนคิ้ว KATE   = 450 THB")
    print("----------------------------------")
    List = int(input("DO YOU WANT TO BUY?"))

    if List == 1:
        price1 = 350
        print("Your order:", List, "price=", price1, "THB")
    elif List == 2:
        price1 = 490
        print("Your order:", List, "price=", price1, "THB")
    elif List == 3:
        price1 = 725
        print("Your order:", List, "price=", price1, "THB")
    elif List == 4:
        price1 = 360
        print("Your order:", List, "price=", price1, "THB")
    elif List == 5:
        price1 = 450
        print("Your order:", List, "price=", price1, "THB")
    else:
        print("Your not order:")
    amount1 = int(input("Do you want to amount?"))

    if List == 1:
        price1 = 350
        print("Total:", List, "price=", price1*amount1, "THB")
    elif List == 2:
        price1 = 490
        print("Total:", List, "price=", price1*amount1, "THB")
    elif List == 3:
        price1 = 725
        print("Total:", List, "price=", price1*amount1, "THB")
    elif List == 4:
        price1 = 360
        print("Total:", List, "price=", price1*amount1, "THB")
    elif List == 5:
        price1 = 450
        print("Total:", List, "price=", price1*amount1, "THB")
    List = int(input("DO YOU WANT TO BUY?"))


    if List == 1:
        price2 = 350
        print("Your order:", List, "price=", price2, "THB")
    elif List == 2:
        price2 = 490
        print("Your order:", List, "price=", price2, "THB")
    elif List == 3:
        price2 = 725
        print("Your order:", List, "price=", price2, "THB")
    elif List == 4:
        price2 = 360
        print("Your order:", List, "price=", price2, "THB")
    elif List == 5:
        price2 = 450
        print("Your order:", List, "price=", price2, "THB")
    else:
        print("Your not order:")
    amount2 = int(input("Do you want to amount?"))

    if List == 1:
        price2 = 350
        print("Total:", List, "price=", price2*amount2, "THB")
    elif List == 2:
        price2 = 490
        print("Total:", List, "price=", price2*amount2, "THB")
    elif List == 3:
        price2 = 725
        print("Total:", List, "price=", price2*amount2, "THB")
    elif List == 4:
        price2 = 360
        print("Total:", List, "price=", price2*amount2, "THB")
    elif List == 5:
        price2 = 450
        print("Total:", List, "price=", price2*amount2, "THB")
    List = int(input("DO YOU WANT TO BUY?"))

    if List == 1:
        price3 = 350
        print("Your order:", List, "price=", price3, "THB")
    elif List == 2:
        price3 = 490
        print("Your order:", List, "price=", price3, "THB")
    elif List == 3:
        price3 = 725
        print("Your order:", List, "price=", price3, "THB")
    elif List == 4:
        price3 = 360
        print("Your order:", List, "price=", price3, "THB")
    elif List == 5:
        price3 = 450
        print("Your order:", List, "price=", price3, "THB")
    else:
        print("Your not order:")
    amount3 = int(input("Do you want to amount?"))

    if List == 1:
        price3 = 350
        print("Total:", List, "price=", price3*amount3, "THB")
    elif List == 2:
        price3 = 490
        print("Total:", List, "price=", price3*amount3, "THB")
    elif List == 3:
        price3 = 725
        print("Total:", List, "price=", price3*amount3, "THB")
    elif List == 4:
        price3 = 360
        print("Total:", List, "price=", price3*amount3, "THB")
    elif List == 5:
        price3 = 450
        print("Total:", List, "price=", price3*amount3, "THB")
    print("All total:",price1*amount1+price2*amount2+price3*amount3,"THB")
    print("----Thank you to all customers for their contribution--")
else:
    print("Error")











