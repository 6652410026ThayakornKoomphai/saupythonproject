# constructor

class DTItest03:
    # data
    infoA = 10

    # constructor จะเป็นตัวทำให้ Obj ที่สร้างจาก class เดียวกันไม่จำเป็นต้องเหมือนกัน
    # constructor จะทำงานทุกครั้งที่มีการสร้าง Obj
    def __init__(self, infoB, infoC):
        self.infoB = infoB
        self.infoC = infoC
        print('wow wow wow ...')

    # method
    def showMixAndInfo(self, mix):
        print(self.infoA + self.infoB + self.infoC + mix)

# สร้าง Object
sau1 = DTItest03(20, 30) 
sau2 = DTItest03(10, 100) 
sau3 = DTItest03(20, 30) 