def inputValue() :
    number = int(input("ป้อนข้อความเลข 1-4 "))
    return number

number = inputValue()

def numberText() :
    if number == 1 :
        greet = "Welcome Freshman"
    elif number == 2 :
        greet = "Welcome Sophomore"
    elif number == 3 :
        greet = "Welcome Junior"
    elif number == 4 :
        greet = "Welcome Senior"    
    else :
        greet = "Invalid number"
    return greet

def showWelcome():
    print(numberText())

showWelcome()