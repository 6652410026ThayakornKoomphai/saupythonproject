# List
my_list = [10,20,30, True, False,"Sale"]
print(my_list)


# Tuple
my_tuple = (10,20,30, True, False,("Sale"))
print(my_tuple)


# Set ไม่มีลำดับ
my_set = {10, 20, 10 ,True, ("hi")}
print(my_set)
print(len(my_set))


for data in my_set:
    print(data, end='/')

print("-------------------------------------")

listformset = list(my_set)
print(listformset)
listformset[0] = "DTI"
my_set = set(listformset)
print(my_set)

my_set.clear()
print(len(my_set))

my_set1 = {10, 20 ,30 ,"hi"}
my_set2 = {10, "hello" ,"hi", True}

my_set1.add(999)
print(my_set1)
my_set1.remove("hi")
print(my_set1)

print(my_set1.intersection(my_set2))
print(my_set1.union(my_set2))

# len, min, max
print(min(my_set2))