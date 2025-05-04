def calculate(a, b,operator):
    match operator:
        case'+':
            return a + b
        case'-':
            return a - b
        case'*':
            return a * b
        case'/':
            if b!=0:
                return a / b
            else:
                return 'Error Division by zero'


a=float(input('Enter 1st no. : '))
b=float(input('Enter 2nd no. : '))
op= input('Enter operator (+, -, *, /)')
result = calculate(a, b, op)
print('Result: ',result)