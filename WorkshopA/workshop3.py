def ProductDetails() :
    productName = input("ใส่ชื่อสินค้า: ")
    productPrice = float(input("ใส่ราคาสินค้า: "))
    return productName, productPrice

productName, productPrice = ProductDetails()

def calculate():
    tax = productPrice * 7 / 100
    return tax

def showCal() :
    print(f"สินค้านี้มีภาษี {calculate()} บาท")

showCal()
