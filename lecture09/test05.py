# คุณสมบัติเด่น Inheritance สืบทอด คือ การที่คลาสนึงสืบทอดกับอีกคลาสนึง *** (re-use)
# สืบทอด มีแม่ (super class/parent) มีลูก (sub class/child)
# แม่มีอะไร ลูกมีด้วย เมื่อมีการสืบทอด (Inheritance)

# คุณสมบัติ Polymorphism (พ้องรูป:พฤติกรรมเดียวแต่วิธีการต่างกัน) คือ การที่คลาสลูกเอาเมธอดคลาสแม่มาเขียนใหม่

class sau01:
    infoA = 10
    
    def showHi():
        print('hi...')

class sau02(sau01): # Inheritance
    infoB = 20

    def showHey():
        print('Hey...')

    # overiding method : Polymorphism
    def showHi():
        print('hi hi hi...')

obj1 = sau01()
obj2 = sau02()
obj2.showHi()

