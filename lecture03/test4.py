money = input("insert amount of money:")
people = input("insert amount of people")
productvalue = int(money)/float(people)
productvaluetext = format(productvalue, ".2f")
print("by average, you would get", productvaluetext, "baht per person.")
print("by average, you would get " + productvaluetext + " baht per person.")
print("by average, you would get {} baht per person.".format(productvaluetext))
print(f"by average, you would get {productvaluetext} baht per person.")