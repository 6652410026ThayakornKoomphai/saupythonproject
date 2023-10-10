def Province():
    province = input("กรอกจังหวัดของคุณ: ")
    return province

def PH():
    ph = int(input("ใส่ค่า PH: "))
    return PH

def pH_Check() :
    Province()
    ph = PH()
    if ph >= 7 and ph < 9 :
        print("ผลลัพธ์เป็นปกติ")
    elif ph > 8 :
        print("ผลลัพธ์เป็นกรด")
    else :
        print("ผลลัพธ์เป็นอัลคาไลน์")

pH_Check()