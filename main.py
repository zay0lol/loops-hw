num = int(input("Enter a number: "))
numdigits = len(str(num))
sumofpowers = sum(int(digit) ** numdigits for digit in str(num))

if sumofpowers == num:
    print("Number is an armstrong number.")
else:
    print( "Number is not an armstrong number.")
