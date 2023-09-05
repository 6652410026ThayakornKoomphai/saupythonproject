#function 2 : have parameter/no return
#parameter คือ ตัวแปร(variable)ประเภทหนึ่ง มีหน้าที่เก็บข้อมูล ต่างกันที่ที่มาของข้อมูล
def funcA(x,y):
    print('aaa')
    z = x + y
    print(f'{x}+{y}={z}')

def funcB(x,y,z):
    print('{:.2f} {:.4f} {:.5f}'.format(x,y,z))

funcA(10,20) #ข้อมูลที่ส่งให้ parameter เรียก argument
funcA(5,10)
funcB(1,5,10)
