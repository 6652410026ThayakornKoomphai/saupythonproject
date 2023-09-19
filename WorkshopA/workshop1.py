def detailproduct() :
    name_product = input("Enter product name: ")
    price_product = float(input("Enter product price: "))
    return name_product, price_product

def calculatePrice() :
    finalproductPrice = price_product + (price_product * 10 / 100)
    return finalproductPrice

def showPrice() :
    print(f"The {name_product} is {calculatePrice()} baht")

productName, productPrice = detailproduct()

showPrice()








