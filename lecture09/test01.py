class DTItest01:
    pass

class DTItest02:
    # data/attribute/property/field คือ ตัวแปรประเภทหนึ่ง
    infoA = ''
    infoB = 20

    # method คือ ฟังค์ชันประเภทหนึ่ง
    def showHi(self):
        print('hi...')

    def showInfoAandB(self):
        print(self.infoA)
        print(self.infoB)

# สร้าง Object
GigachadA = DTItest02()
GigachadB = DTItest02()
GigachadC = DTItest02()


GigachadA.infoA = 'eieiei'
GigachadB.infoB = 100

print(GigachadA.infoB + GigachadB.infoB)

GigachadC.showInfoAandB()