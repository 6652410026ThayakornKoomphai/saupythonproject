var2 = (10, 20, "hello", True, (111,'wow'), "มานะ")

# var2[2] = "hi" error
# การเปลี่ยนแปลงค่า เพิ่ม ลบ ข้อมูลใน Tuple
# list(), tuple()
vartemp = list(var2)
vartemp[2] = "hi"
var2 = tuple(vartemp)
print(var2)