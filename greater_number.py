a, b = map(int, input("Enter two numbers: ").split())

if a > b:
    print("%d is greater" % a)

elif b > a:
    print("%d is greater" % b)

else:
    print("Both numbers are equal")