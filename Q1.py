import math

while True:
    print("Welcome to Mahtab's calculator")
    print("1. Sum")
    print("2. Sub")
    print("3. Mul")
    print("4. Div")
    print("5. sin")
    print("6. cos")
    print("7. tan")
    print("8. cot")
    print("9. log")
    print("10. exit")

    op = int(input("--> "))

    if op == 10:
            break

    elif op == 1 or op == 2 or op == 3 or op == 4 or op == 9:
        a = float(input("a: "))
        b = float(input("b: "))

        if op == 1:
            result = a + b

        elif op == 2:
            result = a - b

        elif op == 3:
            result = a * b

        elif op == 4:
            if b == 0:
                result = "Cannot divide by zero"
            else:
                result = a / b
        
        elif op == 9:
            result = math.log(a, b)

    elif op == 5 or op == 6 or op == 7 or op == 8:
        c = float(input("c: "))

        if op == 5:
            result = math.sin(math.radians(c))

        elif op == 6:
            result = math.cos(math.radians(c))

        elif op == 7:
            result = math.tan(math.radians(c))

        elif op == 8:
            result = 1 / math.tan(math.radians(c))

    else:
         result = "Command not found"

    print(result)