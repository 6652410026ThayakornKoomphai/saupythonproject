def OfficerDetail() :
    officerID = int(input("ใส่พนักงาน ID: "))
    officerName = input("ใส่ชื่อของพนักงาน: ")
    officerSalary = float(input("ใส่เงินเดือนพนักงาน: "))
    return officerID,officerName,officerSalary

officerID,officerName,officerSalary = OfficerDetail()

def netSalaryCalculate() :
    netSalary = officerSalary - (officerSalary * 7 / 100) - 500
    return netSalary

def showNetSalary() :
    print(f"{officerID} {officerName} คุณได้เงินเดือน {netSalaryCalculate()} บาท")

showNetSalary()
