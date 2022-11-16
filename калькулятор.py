a = float(input('Введите чисо:'))
b = float(input('Введите чисо:'))
operation = input('Выберите операцию (+;-):')
if operation == '+':
    c = a + b
    print('Результат'+ str(c))
elif operation == '-':
    c = a - b
    print('Результат'+ str(c))
else:
    print('Выбрана неверная операция')
    