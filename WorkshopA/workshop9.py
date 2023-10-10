def EmpDetails() :
    emp_ID = int(input("ใส่ ID พนักงาน: "))
    emp_Name = input("ใส่ชื่อพนักงาน: ")
    emp_Sales = float(input("ใส่จำนวนราคาที่พนักงานขายได้: "))
    return emp_ID, emp_Name, emp_Sales
  
emp_ID, emp_Name, emp_Sales = EmpDetails()

def commissionCheckAndCal() :
    if emp_Sales < 1000 :
        commission = 0
    elif emp_Sales < 2001 :
        commission = emp_Sales * 1 / 100
    elif emp_Sales < 3001 :
        commission = emp_Sales * 3 / 100
    else :
        commission = emp_Sales * 5 / 100
    return commission

def showCommission() :
    print(f"{emp_ID} {emp_Name} คุณได้ค่าคอมมิชชัน {commissionCheckAndCal()} บาท.")

showCommission()