#variable
# fefe = "dwf Exp"
# ee = "111"
# fgrfr = "fgweete"
# ----------------

# List
                               #0   1
   #  0    1      2         3             4               5       มองจากซ้ายไปขวา
var1 = [10, 20, "hello", True, [111,'wow'], "มานะ"]
   # -6    -5    -4        -3            -2               -1      มองจากขวาไปซ้าย
                               #-2  -1

print(var1[0] + var1[1])
print(var1[-6] + var1[-5])
print(var1[0] + var1[4][0])
print(var1[-6] + var1[-2][-2])

# Tuples
                               # 0    1
   #    0    1     2       3       4          5       มองจากซ้ายไปขวา
var2 = (10, 20, "hello", True, (111,'wow'), "มานะ")
   #    -6  -5    -4      -3      -2          -1      มองจากขวาไปซ้าย
                                #-2  -1

print(var2[0] + var2[1])
print(var2[-6] + var2[-5])
print(f'{var2[2]}....{var2[5]} {var2[4][1]}...') #hello ....มานะ ....wow