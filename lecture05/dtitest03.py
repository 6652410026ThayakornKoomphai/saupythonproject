#function 3 :no parameter/have return
def dti1():
    print(111)
    print(222)
    a,b,c = dti2()
    print(f'สวัสดี {b} อายุ {a} และ {c}')
    return 999

def dti2():
    print(333)
    return 10 + 20, 'สมชาย', True

print( dti1())
x = dti1()
y = dti1() + 111 + 222
print('--------------------')