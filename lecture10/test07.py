# อ่านข้อมูลจากไฟล์
f_dti = open('Myfile02.txt', 'r', encoding='utf-8')

try:
    data = f_dti.read()

    for data_by_line in data:
        print(f'SAU: {data_by_line}', end='')

except Exception:
    print('ติดต่อ admin 09844444')
finally:
    f_dti.close() 