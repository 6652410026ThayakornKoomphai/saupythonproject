def BorrowerDetails() :
    borrowerName = input("ใส่ชื่อผู้กู้เงิน: ")
    MoneyBorrowed = float(input("ใส่จำนวนเงินที่ผู้กู้กู้ไป: "))
    return borrowerName,borrowerMoneyBorrowed

borrowerName,MoneyBorrowed = BorrowerDetails()

def interestCalculate() :
    if MoneyBorrowed > 1000 :
        interest = 2.5 / 100 * MoneyBorrowed
    else :
        interest = 5.5 / 100 * MoneyBorrowed
    return interest

def showInterest() :
    print(f"{borrowerName} คุณต้องจ่าย {interestCalculate()}")

showInterest()
