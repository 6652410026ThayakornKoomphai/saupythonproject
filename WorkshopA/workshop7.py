def inputValueUser() :
    numberInput = float(input("ใส่เลขที่ต้องการของคุณ: "))
    return numberInput

def defineValue() :
    y = "Correct, You are the winner"
    n = "Not Correct!!!"
    return y, n

y,n = defineValue()

def valueCheckAndShow() :
    if inputValueUser() == 25 :
        print(y)
    else :
        print(n)

valueCheckAndShow()