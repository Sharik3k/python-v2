
#маю проблему не хоче запускатись через внутрішній термінал VSC,а працює тільки через зовнішній cmd

number1 = float(input("enter first number:"))
print("operators: + - * /")
op = input("choose operators:")
number2 = float(input("enter second number:"))
if op =="+":
    print("result:",number1 + number2)

elif op =="-":
    print("result:", number1 - number2)

elif op =="*":
    print("result:",number1 * number2)

elif op =="/":
    if number2 != 0:
        print("result:",number1 / number2)
    else:
        print("division by zero is impossible")

else:
    print("Unknown operator")

