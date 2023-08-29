ชื่อ_product = input("ใส่ชื่อ product")
budget = float(input("ใส่ budget product"))

def productvalue(budget):
    product_ราคาจริง = budget + (budget * 10/100)
    return "%.2f" % product_ราคาจริง

print(f"ราคาของ {ชื่อ_product} คือ {productvalue(budget)}") 