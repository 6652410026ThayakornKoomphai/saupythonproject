#โปรแกรมตรวจสอบน้ำหนักรถบรรทุกของด่านช่างน้ำหนักว่ารถบรรทุกนั้นมีน้ำหนักรถผ่านเกณฑ์หรือไม่
#หากน้ำหนักเกิน 1000kg ให้แสดงข้อความว่า "รถน้ำหนักไม่ผ่านเกนณฑ์" แต่หากน้ำหนักตั้งแต่
#1000kg ลงมาให้แสดงข้อความว่า "รถน้ำหนักผ่านเกณฑ์" โดยให้ป้อนทะเบียนรถบรรทุก
#และน้ำหนักรถบรรทุกทางแป้นพิมพ์

#วิเคราะห์
#มองหา feature การทำงานว่ามีอะไรบ้าง เพื่อจะไปสร้างเป็น function
# รับค่าทะเบียนรถ น้ำหนักรถ -> inputCarDetail
# ตรวจสอบน้ำหนักรถ และแสดงผล -> checkCarAndShowWeight

def inputCarDetail():
    carNo = float(input('ป้อนทะเบียนรถ: '))
    carWeight = float(input("ป้อนน้ำหนักรถ: "))
    return carNo, carWeight

def checkCarAndShowWeight(carNo, carWeight):
    if carWeight > 1000:
        print (f'ทะเบียนรถ {carNo} น้ำหนักไม่ผ่านเกณฑ์')
    else:
        print (f'ทะเบียนรถ {carNo} น้ำหนักผ่านเกณฑ์')



print("-----------------------")
print("TruckChecker")
print("-----------------------")

carNom, carWeight = inputCarDetail()
print("--------------------------------")
checkCarAndShowWeight(carNom, carWeight)
print("--------------------------------")      