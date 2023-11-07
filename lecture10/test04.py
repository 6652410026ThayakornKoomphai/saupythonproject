# เขียนข้อมูลลงไฟล์
f_dti = open('Myfile03.txt', 'a', encoding='utf-8') # เปิดไฟล์เพื่อเขียนข้อมูลลงไฟล์

f_dti.write('AAA')
f_dti.write('BBB....\n')
f_dti.write('ลาก่อนทุกคน...\n')

f_dti.close()

print('บันทึกข้อมูลของไฟล์เรียบร้อยแล้ว')