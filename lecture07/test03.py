# List Methods
var1 = [10, 20, "hello", True, [111,'wow'], "มานะ"]
# append เพิ่ม 1 ข้อมูล
var1.append(555)
var1.append(['hi', 'hey', 999])
print(var1)
# extend เพิ่มแต่ละข้อมูล
var1.extend([10,20,30])
print(var1)
# remove เอาข้อมูลออกแต่ออกได้แค่ข้อมูลเดียว
var1.remove('hello')
var1.remove(10)
print(var1)
# -----------------------------
var2 = [10, 20, 'hello']
# insert 
var2.insert(2, 'hi')
print(var2)
# pop
var2.pop()
print(var2) # [10, 20, 'hi']
var2.pop(1)
print(var2)
# index
print(var2.index('hi'))
# count นับจำนวนข้อมูลนั้นๆที่อยู่ใน List
print(var1.count(10))
var3 = [10, 10, 20, 'hi', 10, 'hi']
print(f'ใน var3 มี 10 ทั้งหมด {var3.count(10)} ตัว')
print(f'ใน var3 มี hi ทั้งหมด {var3.count("hi")} ตัว')

# print("hi  'sau'")
# print('hi  "sau"')


# Method ต่อไปนี้ใช้ได้เฉพาะข้อมูลในที่เป็นประเภทเดียวกันเท่านั้น
# sort
var4 = [10, 10, 20, 'hi', 10, 'hi']
# var4.sort()
var5 = [90, 20, 3435, 43546, 141]
print(var5)
var5.sort()
print(var5)
var5.sort(reverse=True)
print(var5)


