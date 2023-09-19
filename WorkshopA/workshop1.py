def inputNamePrice():
    name_product= (input('ป้อนชื่อสินค้า:'))
    price_product = int(input('ป้อนราคาสินค้า:'))
    return name_product, price_product

def calculatePrice():
    price_productReal = price_product + (price_product * 10/100)
    return price_productReal

def showPrice():
    print(f"the {name_product} is {calculatePrice} baht")

name_product , price_product = inputNamePrice()


showPrice()

calculatePrice()









