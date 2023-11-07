# อ่านข้อมูลจากไฟล์
f_dti = open('Myfile01.txt', 'r', encoding='utf-8')

try:
    data = f_dti.readline()
    print(data, end='')
    data = f_dti.readline()
    print(data, end='')

except Exception:
    print('ติดต่อ admin 09844444')
finally:
    f_dti.close() 