# calculator.py
def add(x, y): return x + y
def sub(x, y): return x - y
def mul(x, y): return x * y
def div(x, y): return x / y if y != 0 else "Cannot divide by zero"

print("1.Add  2.Sub  3.Mul  4.Div")
choice = input("Choose (1-4): ")
x, y = map(float, input("Enter two numbers: ").split())

ops = {'1': add, '2': sub, '3': mul, '4': div}
print("Result:", ops[choice](x, y))
