def GroupDetails():
    leader = input("ใส่ชื่อของหัวหน้ากลุ่ม: ")
    leaderTeleNumber = input("ใส่เบอร์โทรหัวหน้ากลุ่ม: ")
    touristmember = int(input("ใส่จำนวนนักท่องเที่ยว: "))
    return leader, leaderTeleNumber, touristmember

leader, leaderTeleNumber, touristmember = GroupDetails()

def calPackage() :
    if touristmember >= 1 and touristmember < 3 :
        package = touristmember * 300
    elif touristmember >= 3 and touristmember < 6 :
        package = touristmember * 250
    elif touristmember >= 6 and touristmember < 11 :
        package = touristmember * 210
    else :
        package = touristmember * 150
        return package

def showPackage():
    print(f"หัวหน้า {leader} เบอร์โทร {leaderNumber} คุณมี {touristmember} แพ็คนักท่องเที่ยวในราคา {calPackage()} บาท")

showPackage()
