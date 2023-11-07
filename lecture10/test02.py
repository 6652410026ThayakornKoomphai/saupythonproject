# เขียนข้อมูลลงไฟล์
f_dti = open('Myfile01.txt', 'w', encoding='utf-8') # เปิดไฟล์เพื่อเขียนข้อมูลลงไฟล์

f_dti.write('wow')
f_dti.write('woo...\n')
f_dti.write('ลาก่อนทุกคน...\n')

f_dti.close()

print('บันทึกข้อมูลของไฟล์เรียบร้อยแล้ว')