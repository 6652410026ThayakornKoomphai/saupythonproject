def inputX():
     x = float(input("ใส่ค่าของ x : "))
     return x

x = inputX()

def calculate():
     y = 2 * x ** 2 + 2 * x + 1
     return y

def showCal():
      print(f"ค่าของ y {calculate()}")

showCal()
