def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'
        
    operators = ['+','-']

    top_line=[]
    bottom_line=[]
    dash_line = []
    ans_line = []

    for problem in problems:
        equation_parts = problem.split()
        if len(equation_parts) != 3:
            print('Invalid Input')
        
        operand1,operator,operand2 = equation_parts
        
        if not operand1.isdigit() or not operand2.isdigit():
            return 'Error: Numbers must only contain digits.'


        if len(operand1) > 4 or len(operand2) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        if operator not in operators:
            return "Error: Operator must be '+' or '-'."

        width_size= max(len(operand1), len(operand2)) + 2

        top_align = operand1.rjust(width_size)
        bottom_align = operator + operand2.rjust(width_size - 1)
        dash ='-' * width_size

        top_line.append(top_align)
        bottom_line.append(bottom_align)
        dash_line.append(dash)

        if show_answers:
            if operator == '+':
               result = str(int(operand1)+int(operand2))
            else:
                result = str(int(operand1)-int(operand2))
            ans_line.append(result.rjust(width_size))

    top_line_string = '    '.join(top_line)
    bottom_line_string = '    '.join(bottom_line)
    dash_string = '    '.join(dash_line)

    if show_answers:
        ans_string = '    '.join(ans_line)
        return f'{top_line_string}\n{bottom_line_string}\n{dash_string}\n{ans_string}'
    else:
        return f'{top_line_string}\n{bottom_line_string}\n{dash_string}'

print('Welcome to the Arithmetic Formatter!\n')
print('example: 32 + 698, 3801 - 2, 45 + 43, 123 + 49, 1 - 3801\n')

equation = []
user_input = input('Enter the arithmetic problems separated by commas as shown in the example: ')
equation = user_input.split(',')  # Split input string into a list of problems using comma as separator

print(f'\n{arithmetic_arranger(equation, True)}')