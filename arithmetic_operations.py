a, b = map(int, input("Enter two numbers: ").split())

add = a + b
sub = a - b
mul = a * b

print("Addition = %d" % add)
print("Subtraction = %d" % sub)
print("Multiplication = %d" % mul)

if b != 0:
    div = a / b
    print("Division = %.2f" % div)
else:
    print("Division is not possible by zero.")