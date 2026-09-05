# simple calculator

def simple_calculator(n1: int, n2: int, op: str) -> float:
    """
    Docstring: This function receives two integers as operands
    and an operator as string, then calculates the result and
    returns based on that!
    """

    print('- Entered calculator function')

    if op not in ['*','+','/','-']:
        raise ValueError("Invalid operator entered!")

    if op == '/' and n2 == 0:
        raise ValueError("This would cause division by zero!")

    calc_switch = {
        '*' : n1*n2,
        '/' : n1/n2,
        '+' : n1+n2,
        '-' : n1-n2
    }
    
    print('- Returning calculation')
    return calc_switch.get(op)

print('- Program begins')

try:
    number1 = int(input('Enter number1: '))
    number2 = int(input('Enter number2: '))
except ValueError:
    raise ValueError('Operands type mismatch!')

try:
    operator = input('Enter operator: ')
except ValueError:
    raise ValueError('Operator mismatch!')


print(f"\nResult: {simple_calculator(number1, number2, operator)}")


