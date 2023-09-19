def UserDetails() :
    user_Name = input("ใส่ชื่อของผู้ใช้: ")
    user_Tele = float(input("ใส่เบอร์โทรของผู้ใช้: "))
    user_Times = float(input("ใส่เวลาในการใช้โทรของผู้ใช้: "))
    return user_Name, user_Tele, user_Times

user_Name, user_Tele, user_Times = getUserDetails()

def calculateServiceCost() :
    if user_Times >= 1 and user_Times < 16 :
        serviceCost = user_Times * 5
    elif user_Times >= 16 and user_Times < 31 :
        serviceCost = user_Times * 3
    else :
        serviceCost = user_Times * 1.5 
    return serviceCost

def showServiceCost() :
    print(f"{userName} เบอร์โทร {userTel} คุณมีค่า service charge {calculateServiceCost()}")

showServiceCost()
