#function 4: have parameter/have return
def dti1(a,b):
    print(f'{a} ยกกำลัง {b} = {a ** b}')
    return a ** b

def dti2(a,b,x,y):
    return a + b + x + y + dti1(2,3) , ' wow wow wow'


x,y = dti2(2 ,4 ,6 ,8)

print(f'{x} ^_^ {y}')