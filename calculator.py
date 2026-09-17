
def calculate():
    x = int(input("Enter 1st number:"))
    y = int(input("Enter 2nd number:"))
    a = input("Enter your choice(+,-,*,/)")
    match(a):
        case "+":
            print(x+y)
        case "-":
            print(x-y)
        case "*":
            print(x*y)
        case "/":
            print(x/y)
calculate()               
