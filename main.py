'''result_1 = None
operand_1 = None
operand_2 = None
operator = None
wait_for_number = True

while True:'''

operand_2 = int(input('Enter an integer:'))
operator = input('Enter operation:')
operand_1 = input('Enter an integer:')
int(operand_1)
if  operand_1 is int and operand_2 is int and operator == '+':
    result_1 = operand_1 + operand_2
elif operand_1 is not int:
    operand_1 = int(input('Enter an integer:'))
    result_1 = operand_1 + operand_2
elif operand_2 is not int:
    operand_1 = int(input('Enter an integer:'))
    result_1 = operand_1 + operand_2
print ((f"{operand_1} {operator} {operand_2} = {result_1}"))





    

