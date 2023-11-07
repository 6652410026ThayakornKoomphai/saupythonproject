# เขียนข้อมูลลงไฟล์
f_dti = open('Myfile02.txt', 'x', encoding='utf-8') # เปิดไฟล์เพื่อเขียนข้อมูลลงไฟล์

f_dti.write('SAU555')
f_dti.write('DTI555...\n')
f_dti.write('ลาก่อนทุกคน...\n')

f_dti.close()

print('บันทึกข้อมูลของไฟล์เรียบร้อยแล้ว')