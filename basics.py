a = int(input("enter the first number :"))
b = int(input("enter the second number :"))
c = str(input("select a operator, "
              "+, -, x, /  :"))
if c == "+":
    print(a+b)
elif c == "-":
    print(a-b)
elif c == "x":
    print(a*b)
elif c == "/":
    print(a//b)
else:
    print("wrong operator")
