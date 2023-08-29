#Function แบบที่ 2 - Have parameters/No return
#parameters คือ ตัวแปรประเภทหนึ่ง เอาไว้รับค่ามาใช้เฉพาะใน function นั้นๆ เท่านั้น

def funcA(x,y) :
    print(f'X is {x}')
    print(f'Y is {y}')
    print(f'Sum {x} + {y} = {x+y}')

funcA(10,20) #call function ข้อมูลที่ส่งให้ parameter เรียกว่า argument
funcA(1, 4)
print('DTI..........')
funcA(4,7)