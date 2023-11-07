try:
    num1 = int(input('ป้อนตัวเลข 1 :'))
    num2 = int(input('ป้อนตัวเลข 2 :'))

    result1 = num1 * num2
    result2 = num1 / num2

    print(f'{num1} x {num2} = {result1}')
    print(f'{num1} / {num2} = {result2}')
except ValueError :
    print('ตรวจสอบการป้อนข้อมูล เนื่องจากข้อมูลที่ไม่ถูกต้อง') 
except ZeroDivisionError :
    print('เนื่องจากไม่มีตัวเลขตัวไหนที่หารด้วย 0 ได้ กรุณากรอกข้อมูลตัวเลขที่ไม่ใช่ 0')
except Exception :
    print('มีข้อผิดพลาดเกิดขึ้น กรุณาติดต่อ 025999999 หรือติดต่อทีม IT')
finally :
    print('wow woo ewee')
