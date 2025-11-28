accepted_opeartor = ['+', '-', '*', '/']
operator = input("Enter an operator( + - * /): ")

while True:
    if operator not in accepted_opeartor:
        print("We don't accept any other opeartor")
        break
    
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    total = 0
    match operator:
        case "+":
            total += num1 + num2

        case "-":
            total += num1 - num2
        
        case "*":
            total += num1 * num2
        
        case "/":
            total += num1 / num2

    print(f" {num1} {operator} {num2} = {total}")


