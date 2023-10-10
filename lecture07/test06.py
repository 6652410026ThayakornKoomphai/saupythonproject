# slicing data in List and Tuple

var1 = [10, 20, "hello", True, [111,'wow'], "มานะ"]
var2 = (10, 20, "hello", True, (111,'wow'), "มานะ")

# 20, 'hello, True
print(var1[1:4])
# True, (111,'wow)
print(var2[3:5])
# 10, 20, 'hello'
print(var1[:3])
# 'hello, True, (111,'wow'), "มานะ"
print(var1[2:])