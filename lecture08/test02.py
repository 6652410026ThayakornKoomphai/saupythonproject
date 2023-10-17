# list มีลำดับ
my_list = [10,20,30, True, (10,"hello" ),[10,20],{"SAU","DTI"}]

# tuple มีลำดับ
my_tuple = (10,20,30, True,(10,"hello" ),[10,20],{"SAU","DTI"})

# set ไม่มีลำดับ
my_set = {10, 20, 10 ,True, ("hi")}


                   #Key: คือ index คือ ตัวชี้ที่อ้างอิงไปยัง Value
                   #Value: คือ ค่าข้อมูลที่สามารถใช้งานได้

# Dictionary --->> Key-Value / key -> String Number / Value -> Everything
my_Dic = {"name":"สมชาย", "age":20, 555:999, "flag":True}
print(my_Dic["name"])
print(my_Dic["age"] + my_Dic[555])
my_Dic["name"] = "สมหญิง"
my_Dic["major"] = "DTI"
print(my_Dic)
my_Dic.pop("name")
my_Dic.pop(555)
print(my_Dic)
my_Dic.popitem
print(my_Dic)




for data in my_Dic:
    print(data, end=" ")

print()

for data in my_Dic.keys():
    print(data, end=" ")

print()

for data in my_Dic.values():
    print(data, end=" ")

my_Dic1 = {"A":70, "B":20, "C":30}

my_Dic2 = my_Dic1

my_Dic3 = my_Dic1.copy()


print()
print(my_Dic1)
print(my_Dic2)
my_Dic2["A"] = 999
my_Dic3["A"] = 999
print("--------------------------")
print(my_Dic1)
print(my_Dic2)
print(my_Dic3)




