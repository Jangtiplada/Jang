#โจทย์ดังภาพนี้
#input= 5
#output
#       *
#      * *
#     * * *
#    * * * *
#   * * * * *

Number =  int(input("Enter the number of rows:"))
for i in range(0,Number):
    for x in range (0,Number-i-1):
        print(end= " ")
    for x in range(0,2*i+1):
        print("*",end="")
    print( )