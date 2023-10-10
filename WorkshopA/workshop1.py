def detailproduct() :
    name_product = input("Enter product name: ")
    price_product = float(input("Enter product price: "))
    return name_product, price_product

def calculatePrice() :
    finalproductPrice = productPrice + (productPrice * 10 / 100)
    return finalproductPrice

def showPrice() :
    print(f"The {productName} is {calculatePrice()} baht")

productName, productPrice = detailproduct()

showPrice()