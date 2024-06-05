Num1 = int(input('Num1: '))
Num2 = int(input('Num2: '))
Num3 = int(input('Num3: '))

if Num1 == Num2 and Num2 == Num3:
    print('3')
elif Num1 == Num2 or Num1 == Num3 or Num2 == Num3:
    print('2')
else:
    print('0')