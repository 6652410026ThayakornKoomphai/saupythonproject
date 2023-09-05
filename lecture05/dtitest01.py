#Function 1: No parameter/No return
def funcA():
    print('AAA')
    #funcB():ไม่ควรเรีนกฟังค์ชันกันไปมา
    print("www")
    #No return คือไม่มีคำสั่ง return

def funcB():
    print(123)
    funcA()

funcA()
funcB()
funcB()
funcA()
    