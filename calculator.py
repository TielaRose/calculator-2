"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# while exit_condition_not_reached:
#     input = consume_input()
#     output = evaluate_input(input)
#     print(output)

while True:
    # get user input in the form [operation] [num1] [num2]
    input_string = input('What do you want to calculate? ')
    # sample input would be '+ 1 2'

    # separate the input string into usable parts
    input_tokens = input_string.split(' ')
    operation = input_tokens[0]

    if 'q' in operation:
        print('You will exit')
        break
    else:
        num1 = int(input_tokens[1])
        num2 = int(input_tokens[2])

        if operation == '+':
            output = float(add(num1, num2))

        elif operation == '-':
            output = float(subtract(num1, num2))

        elif operation == '*':
            output = float(multiply(num1, num2))

        elif operation == '/':
            output = float(divide(num1, num2))

    print(output)
