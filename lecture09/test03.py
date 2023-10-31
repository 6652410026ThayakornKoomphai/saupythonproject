# Destructor
class DTItest04:
    data1 = 10 

    # constructor
    def __init__(self, data2):
        self.data2 = data2
        print('hi...')
    def doTask1(self):
        print('^_^')
    def doTask2(self, value):
        print(value)

    # destructor    
    def __del__(self):
        print('bye bye...')


# --------------------------------------
sauA = DTItest04(20)
sauB = DTItest04(30)
sauC = DTItest04(20)

sauC.doTask2('T_T')
sauC.doTask1()
print(sauA.data1 + sauB.data1)
    