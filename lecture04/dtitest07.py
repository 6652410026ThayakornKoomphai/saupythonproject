ID = input("ใส่เลข ID: ")
Name = input("ใส่ชื่อ")
Salary = float(input("salary:"))

tax_minus = Salary - (Salary * 7/100) - 500
tax_minus_lowerfloat = "%.2f" % tax_minus

print(f"ID {ID} Mr/Miss {Name} Your salary is {tax_minus_lowerfloat}")